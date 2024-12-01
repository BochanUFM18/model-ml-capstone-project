import os
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, request, jsonify
import pandas as pd

model = tf.keras.models.load_model('model/NutriCheck_model.h5')
nutrition_data = pd.read_csv("dataset/nutrition_clean_dataset.csv")

class_names = [
    "Tempeh", "bibimbap", "cheesecake", "chicken Soto", "chicken noodle",
    "chicken porridge", "chicken wings", "chocolate_cake", "churros",
    "cup_cakes", "donuts", "fish_and_chips", "french_fries",
    "french_toast", "fried shrimp", "fried_rice", "gado-gado",
    "green bean porridge", "grilled chicken", "gyoza", "hamburger",
    "hot_dog", "ice_cream", "ikan bakar", "kupat tahu", "lasagna",
    "macaroni_and_cheese", "macarons", "meatball", "nasi kuning",
    "nasi uduk", "omelette", "oxtail soup", "oysters", "pad_thai",
    "pancakes", "pizza", "ramen", "red_velvet_cake", "rendang",
    "risotto", "samosa", "sashimi", "satay", "spaghetti_bolognese",
    "spaghetti_carbonara", "spring_rolls", "steak", "sushi", "tacos",
    "takoyaki", "tiramisu", "waffles",
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
    

@app.route("/nutrition", methods=["GET"])
def get_nutrition():
    food_name = request.args.get("food", None)
    if not food_name:
        return jsonify({"error": "Food name is required as a query parameter"}), 400

    # Filter nutrition data
    food_info = nutrition_data[nutrition_data["Food Name"].str.contains(
        food_name, case=False, na=False)]
    if food_info.empty:
        return jsonify({"error": "Food not found"}), 404

    # Convert to JSON
    food_data = food_info.iloc[0].to_dict()
    return jsonify({
        "Food ID": food_data["Food ID"],
        "Food Name": food_data["Food Name"],
        "Calories": food_data["Calories"],
        "Serving Size": food_data["Serving Size"],
        "Serving Size (grams)": food_data["Serving Size (grams)"],
        "nutritions": {
            "Calcium": food_data["Calcium"],
            "Dietary Fiber": food_data["Dietary Fiber"],
            "Iron": food_data["Iron"],
            "Protein": food_data["Protein"],
            "Total Carbohydrate": food_data["Total Carbohydrate"],
            "Vitamin A": food_data["Vitamin A"],
            "Vitamin B": food_data["Vitamin B"],
            "Vitamin C": food_data["Vitamin C"],
        }
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("port", 8080)))
