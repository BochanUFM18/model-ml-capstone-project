from flask import Flask, request, jsonify
import tensorflow as tf  # Sesuaikan dengan library yang Anda gunakan

app = Flask(__name__)

# Load model ML
model = tf.keras.models.load_model('D:\mode-ml\ML_NutriCheck\model\NutriCheck_model.h5')  # Sesuaikan dengan format model Anda

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Preprocessing input data sesuai dengan model Anda
    input_data = data['input']
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

