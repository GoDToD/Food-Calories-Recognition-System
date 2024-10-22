import onnx
import onnxruntime as ort
from services.food_calories_data import food_calories
import numpy as np
import torch
import cv2

ALLOWERD_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ORT_SESSION = ort.InferenceSession('model/best.onnx')

def preprocess_image(image, input_size=(320, 320)):
    # Resize to 320x320
    image = cv2.resize(image, input_size)
    # Normalize pixel values (0-1)
    image = image.astype(np.float32) / 255.0
    # Convert to CHW format (channels, height, width)
    image = np.transpose(image, (2, 0, 1))
    # Add batch dimension (batch_size, channels, height, width)
    image = np.expand_dims(image, axis=0)
    return image

# Inference function
def run_inference(image):
    # Preprocess image
    input_tensor = preprocess_image(image)
    
    # Get input and output names for the ONNX model
    input_name = ORT_SESSION.get_inputs()[0].name
    outputs = ORT_SESSION.run(None, {input_name: input_tensor})
    
    return outputs  

def post_process(outputs, conf_thres=0.5):
    # YOLOv8 typically outputs [batch_size, num_boxes, num_attributes]
    # where num_attributes includes (x, y, w, h, obj_conf, class_scores)
    predictions = outputs[0]
    print("PREDICTIONS:", predictions)
    # Apply sigmoid to object confidence and class scores
    predictions[..., 4:] = torch.sigmoid(torch.tensor(predictions[..., 4:]))
    
    # Filter out predictions with low object confidence
    conf_mask = predictions[..., 4] > conf_thres
    predictions = predictions[conf_mask]
    
    # Get the class with the highest score (argmax along class axis)
    class_ids = torch.argmax(predictions[..., 5:], dim=-1).numpy()
    confidences = predictions[..., 4].numpy()  # Object confidence scores
    print("CSERERERER:",class_ids, confidences)
    return class_ids, confidences

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWERD_EXTENSIONS

def recognize_image(file):
    np_img = np.fromfile(file, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    raw_output = run_inference(img)

    predictions = post_process(raw_output, img.shape)

    print(predictions)
    food_name = 'food_name'
    calories = '100kcal per 100g'
    return food_name, calories

def model_details():
    model = onnx.load('model/best.onnx')
    graph = model.graph
    # Inspect the inputs
    print("Model inputs:")
    for input in graph.input:
        print(f"Name: {input.name}")
        print(f"Type: {input.type.tensor_type}")
        dims = [dim.dim_value for dim in input.type.tensor_type.shape.dim]
        print(f"Shape: {dims}")

    # Inspect the outputs
    print("\nModel outputs:")
    for output in graph.output:
        print(f"Name: {output.name}")
        print(f"Type: {output.type.tensor_type}")
        dims = [dim.dim_value for dim in output.type.tensor_type.shape.dim]
        print(f"Shape: {dims}")
    return ""