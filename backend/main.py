from flask import Flask, jsonify, request
from services.utils import allowed_file, recognize_image
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['upload_folder'] = './uploaded_images'

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/upload_image', methods=['GET'])
def get_upload_image():
    return jsonify({"message": "Upload Image"})

@app.route('/api/upload_image', methods=['POST'])
def post_upload_image():
    file = request.files['file']
    file.save(f'./uploaded_images/{file.filename}')
    food_name, calories = recognize_image(f'./uploaded_images/{file.filename}')
    return jsonify({"message": "Upload Image", "food_name": food_name, "calorise": calories})

if __name__ == '__main__':
    app.run(debug=True)