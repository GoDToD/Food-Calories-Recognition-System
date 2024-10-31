from flask import Flask, jsonify, request
from flask_cors import CORS
from services.utils import allowed_file, recognize_image, model_details
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['upload_folder'] = './uploaded_images'

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API server is running"})

@app.route('/api/upload_image', methods=['GET'])
def get_upload_image():
    return jsonify({"message": "Upload Image"})

@app.route('/api/model_details', methods=['GET'])
def get_model_details():
    model_details()
    return jsonify({"message": "Model Details"})

@app.route('/api/upload_image', methods=['POST'])
def post_upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    results = recognize_image(file)
    return jsonify({"message": "Recognised", "results": results})

if __name__ == '__main__':
    app.run(debug=True,port=7766)