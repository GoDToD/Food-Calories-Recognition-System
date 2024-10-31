# Food Calories Recognition System

## Overview

The **Food Calories Recognition System** is an innovative AI-powered solution designed to simplify the process of tracking calorie intake. Utilizing advanced object detection technology, specifically **YOLOv8**, the system accurately recognizes different types of food from images uploaded by users and estimates calories per 100 grams.

## Frontend & Backend Applications

- **Frontend**: Developed with the **React** framework, the frontend communicates with the backend via APIs.
- **Backend**: The backend is developed using **Flask**. The food images will be sent from the frontend to the backend, and the results will return to the frontend application in JSON format.

## Deployment

The system is deployed on **Windows 11**. To run the backend of the system, ensure you have a working Python installation with the necessary libraries installed:

- Flask
- Flask-Cors
- Flask-requests
- OpenCV-python
- Onnx
- Onnxruntime
- Torch
- Torchaudio
- Torchvision
- Ultralytics

### Installing Required Libraries

To install the libraries listed above, run the following command in your terminal:

```bash
pip install <library_name>
```

### Running the Backend

1. Open a terminal and navigate to the backend directory:
   ```bash
   cd <path_to_system>/Food-Calories-Recognition-System/backend
   ```
2. Start the backend service:
   ```bash
   python main.py
   ```

### Running the Frontend

Next, you need to run the frontend application, which requires **Node.js** installation. After installing Node.js, follow these steps:

1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd <path_to_system>/Food-Calories-Recognition-System/frontend/food_calories_recognition_frontend
   ```
2. Install the frontend dependencies:
   ```bash
   npm install
   ```
3. Start the frontend application:
   ```bash
   npm start
   ```

## Accessing the System

Open your browser and go to `http://127.0.0.1:3000/`. This will take you to the home page of the system, where you can upload food images. The system supports the following image formats: **JPG, JPEG, and PNG**.

To upload an image, click the **“Click Here to Start your new life”** button to navigate to the upload page.

### Uploading an Image

On the upload page, you can upload your image by clicking the **“Click Here to Upload Image”** button.

### Viewing Results

Once the detection is complete, you will be redirected to the results page, where the names of the detected foods and their related calorie information will be displayed.

