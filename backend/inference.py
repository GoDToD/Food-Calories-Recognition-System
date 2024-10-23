from ultralytics import YOLO
from services.food_calories_data import food_calories, food_labels

# # Load the YOLO11 model
# model = YOLO("yolo11n.pt")

# # Export the model to ONNX format
# model.export(format="onnx")  # creates 'yolo11n.onnx'

# Load the exported ONNX model
onnx_model = YOLO(r"model\best.onnx", task="detect")

# Run inference with the correct input size
#results = onnx_model.predict("D:\projects\Food\data\images\\train\waffles_3852270.jpg", imgsz=(320, 320))
results = onnx_model.predict(r"waffles_3855881.jpg", imgsz=(320, 320))
for result in results:
    # Extract the class IDs and map them to names
    class_ids = result.boxes.cls.cpu().numpy().astype(int)  # Extract the class IDs
    class_names = [result.names[class_id] for class_id in class_ids]  # Map class IDs to names

    # Print the detected class names
    for class_name in class_names:
        
        calories = food_calories[class_name]
        print("Detected classes:", class_name)
        print("Detected calories", calories)
        
      