import onnx
import onnxruntime as ort
from services.food_calories_data import food_calories
import numpy as np
import cv2

ALLOWERD_EXTENSIONS = {'png', 'jpg', 'jpeg'}
ORT_SESSION = ort.InferenceSession('model/best.onnx')

def preprocess_image(image, input_size=(320, 320)):
    # Resize image
    resized = cv2.resize(image, input_size)
    # Normalize image to [0, 1]
    #normalized = resized / 255.0
    # Transpose the image to [channels, height, width]
    #transposed = np.transpose(normalized, (2, 0, 1))
    transposed = np.transpose(resized, (2, 0, 1))
    # Add batch dimension [batch_size, channels, height, width]
    batch = np.expand_dims(transposed, axis=0).astype(np.float32)
    return batch

# Inference function
def run_inference(image):
    # Preprocess image
    input_tensor = preprocess_image(image)
    
    # Get input and output names for the ONNX model
    input_name = ORT_SESSION.get_inputs()[0].name
    outputs = ORT_SESSION.run(None, {input_name: input_tensor})
    
    return outputs

def postprocess_output(output, img_shape, confidence_threshold=0.5):
    # Assuming output is a list of predictions for a single image
    # and img_shape is the original shape of the image.
    predictions = []
    
    for pred in output[0]:  # Assuming batch size is 1
        x, y, w, h, conf = pred[:5]
        class_scores = pred[5:]
        
        if conf < confidence_threshold:
            continue
        
        class_id = np.argmax(class_scores)
        confidence = conf
        # Convert normalized coords back to the original image shape
        x = int(x * img_shape[1])
        y = int(y * img_shape[0])
        w = int(w * img_shape[1])
        h = int(h * img_shape[0])
        
        predictions.append({
            "bounding_box": [x, y, w, h],
            "confidence": float(confidence),
            "class": int(class_id)  # You can map class_id to actual class names
        })
    
    return predictions

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWERD_EXTENSIONS

def recognize_image(file):
    np_img = np.fromfile(file, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    raw_output = run_inference(img)
    print(raw_output)

    predictions = postprocess_output(raw_output, img.shape)

    print(predictions)
    food_name = 'food_name'
    calories = '100kcal per 100g'
    return food_name, calories

def model_details():
    # print(MODEL)
    return ""