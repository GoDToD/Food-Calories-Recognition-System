import onnxruntime as ort
import numpy as np
import cv2  # For image preprocessing
from services.food_calories_data import food_calories, food_labels

# Load the ONNX model
session = ort.InferenceSession("model/best.onnx")

# Load and preprocess the image
def preprocess_image(image_path, input_size=(320, 320)):
    # Load image
    image = cv2.imread(image_path)
    
    # Resize to the input size
    image_resized = cv2.resize(image, input_size)
    
    # Normalize the image (YOLOv8 expects [0, 1] range for input)
    image_normalized = image_resized / 255.0
    
    # Convert the image to CHW format (channels, height, width)
    image_transposed = np.transpose(image_normalized, (2, 0, 1)).astype(np.float32)
    
    # Add a batch dimension (1, channels, height, width)
    image_batch = np.expand_dims(image_transposed, axis=0)
    
    return image_batch

def post_process_image(outputs):
    
    # YOLOv8 typically outputs [batch_size, num_boxes, num_attributes]
    # where num_attributes includes (x, y, w, h, obj_conf, class_scores)
    predictions = outputs[0]
    print("prediction:",predictions.shape)
    print(predictions[0][0][4:])
    
    # Apply sigmoid to object confidence and class scores
    predictions[...,4:] = 1 / (1 + np.exp(-predictions[...,4:]))
    print("prediction:",predictions.shape)
    print(predictions[0][0][4:])
    
    # Filter out predictions with low object confidence
    confidence_mask = predictions[...,4] > 0.5
    predictions = predictions[confidence_mask]
    print("prediction:",predictions.shape)
    
    # Get the class with the highest score (argmax along class axis)
    class_ids = np.argmax(predictions[...,5:], axis=-1)
    print(predictions)
    confidences = predictions[...,4]
    boxes = predictions[..., :4 ]
    
    return class_ids, confidences, boxes

def post_process(outputs):

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


# Preprocess your image
image_path = "waffles_3855881.jpg"
input_tensor = preprocess_image(image_path)

# Run inference
outputs = session.run(None, {"images": input_tensor})

print(outputs)
print("test:")
post_process(outputs)
print("real:")
class_id, confidence = post_process(outputs)
print("class_ids:",class_id)
class_name = food_labels[class_id]
calories = food_calories[class_name]

print(class_name)
print(calories)