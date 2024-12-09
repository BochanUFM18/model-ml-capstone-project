import os
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request, jsonify

model = tf.keras.models.load_model('model/NutriCheck_model.h5')

class_names = [
    "Bibimbap",
    "Cheesecake",
    "Chicken Noodle",
    "Chicken Porridge",
    "Chicken Soto",
    "Chicken Wings",
    "Chocolate Cake",
    "Churros",
    "Cupcakes",
    "Donuts",
    "Fish and Chips",
    "French Fries",
    "French Toast",
    "Fried Rice",
    "Fried Shrimp",
    "Gado-Gado",
    "Green Bean Porridge",
    "Grilled Chicken",
    "Gyoza",
    "Hamburger",
    "Hot Dog",
    "Ice Cream",
    "Ikan Bakar",
    "Kupat Tahu",
    "Lasagna",
    "Macaroni and Cheese",
    "Macarons",
    "Meatball",
    "Omelette",
    "Oxtail Soup",
    "Oysters",
    "Pad Thai",
    "Pancakes",
    "Pizza",
    "Ramen",
    "Red Velvet Cake",
    "Rendang",
    "Risotto",
    "Samosa",
    "Sashimi",
    "Satay",
    "Spaghetti Bolognese",
    "Spaghetti Carbonara",
    "Spring Rolls",
    "Steak",
    "Sushi",
    "Tacos",
    "Takoyaki",
    "Tempeh",
    "Tiramisu",
    "Uduk Rice",
    "Waffles",
    "Yellow Rice"
]

app = Flask(__name__)


def preprocess_image(image):
    image = image.convert("RGB")  # Konversi ke RGB
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file found"}), 400

    image_file = request.files["image"]
    if image_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    try:
        image = Image.open(image_file)
        image_array = preprocess_image(image)

        prediction = model.predict(image_array)

        predicted_class_idx = np.argmax(prediction[0])
        predicted_class = class_names[predicted_class_idx]

        return jsonify({
            "status": 200,
            "message": "Prediction successful",
            "food_name": predicted_class
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("port", 8080)))
