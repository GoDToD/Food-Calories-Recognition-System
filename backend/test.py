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

def save_output_to_txt(output_file, class_ids, scores, boxes):
    with open(output_file, 'w') as f:
        # Iterate over the detected objects and write to file
        for i in range(len(class_ids)):
            class_id = int(class_ids[i])
            confidence = float(scores[i])
            
            # Bounding box coordinates
            x_center, y_center, width, height = boxes[i]
            
            # Convert normalized values to the actual dimensions of the image
            x_center = int(x_center * 320)
            y_center = int(y_center * 320)
            width = int(width * 320)
            height = int(height * 320)

            # Write to file in a structured format
            f.write(f"Object {i + 1}:\n")
            f.write(f"Class ID: {class_id}\n")
            f.write(f"Confidence: {confidence:.4f}\n")
            f.write(f"Bounding Box: [x_center: {x_center}, y_center: {y_center}, width: {width}, height: {height}]\n")
            f.write("\n")  # Add a newline between each object's data

def post_process(outputs):
    
    # YOLOv8 typically outputs [batch_size, num_boxes, num_attributes]
    # where num_attributes includes (x, y, w, h, obj_conf, class_scores)
    predictions = outputs[0]
    
    # Apply sigmoid to object confidence and class scores
    predictions[..., 4:] = 1 / (1 + np.exp(-predictions[..., 4:]))
    
    # Filter out predictions with low object confidence
    conf_mask = predictions[..., 4] > 0.5
    predictions = predictions[conf_mask]
    
    # Get the class with the highest score (argmax along class axis)
    class_ids = np.argmax(predictions[..., 5:], axis=-1)
    confidences = predictions[..., 4]
    boxes = predictions[..., :4]
    
    return class_ids, confidences, boxes

# Preprocess your image
image_path = "image.jpg"
input_tensor = preprocess_image(image_path)

# Run inference
outputs = session.run(None, {"images": input_tensor})

print(outputs)

class_ids, confidences, boxes = post_process(outputs)
id_not_zero = [class_id for class_id in class_ids if class_id != 0]
class_names = [food_labels[class_id] for class_id in id_not_zero]
calories = [food_calories[class_name] for class_name in class_names]

print(class_names)
print(calories)