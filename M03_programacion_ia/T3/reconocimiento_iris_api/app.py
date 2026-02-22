from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo al inicio
model = joblib.load('iris_model.pkl')
class_names = joblib.load('class_names.pkl')

@app.route('/')
def home():
    return "Bienvenido a la API de Clasificación de Iris. Usa el endpoint /predict."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # El modelo espera una lista de 4 valores: [sepal_l, sepal_w, petal_l, petal_w]
        prediction = model.predict([data['features']])
        label = class_names[prediction[0]]
        
        return jsonify({
            'prediction_index': int(prediction[0]),
            'prediction_label': label
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)