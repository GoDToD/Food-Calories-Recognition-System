ALLOWERD_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWERD_EXTENSIONS

def recognize_image(image_path):
    food_name = 'food_name'
    calories = '100kcal per 100g'
    return food_name, calories