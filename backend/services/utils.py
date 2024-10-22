import onnx
import onnxruntime as ort
from services.food_calories_data import food_calories, food_labels
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
    predictions = outputs[0]
    print("prediction:",predictions.shape)
    predictions = predictions[0]
    predictions = np.transpose(predictions)
    print("prediction:",predictions)
    print("prediction:",predictions.shape)
    print(predictions[210])

    (i,j) = predictions.shape

    new_predictions = np.zeros((i, 6))

    for a in range(i):
        max_confidence = np.max(predictions[a][5:])
        max_index = np.argmax(predictions[a][5:])
        new_predictions[a] = np.concatenate((predictions[a][0:4], [max_confidence], [max_index]))

    print("new_predictions:",new_predictions)

    best_prediction = new_predictions[np.argmax(new_predictions[:,4])]

    print("best_prediction:",best_prediction)

    best_class = best_prediction[5]
    best_confidence = best_prediction[4]

    return int(best_class), best_confidence

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWERD_EXTENSIONS

def recognize_image(file):
    np_img = np.fromfile(file, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    raw_output = run_inference(img)

    class_id, best_confidence = post_process(raw_output)

    food_name = food_labels[class_id]
    calories = food_calories[food_name]
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