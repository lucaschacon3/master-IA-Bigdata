# ==============================================================================
# DESPLIEGUE: API de Inferencia con Flask
# ==============================================================================

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# --- CARGA DE ARTEFACTOS ---
# Cargamos el "cerebro" (modelo) y la "fábrica de limpieza" (preprocesador)
try:
    model = joblib.load('modelo_final.pkl')
    preprocessor = joblib.load('preprocesador.pkl')
    print("✔ Modelo y Preprocesador cargados correctamente.")
except Exception as e:
    print(f"❌ Error al cargar artefactos: {e}")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para recibir datos de una casa en formato JSON
    y devolver la predicción de precio.
    """
    try:
        # 1. Obtener datos del JSON enviado por el cliente
        data = request.get_json()
        
        # 2. Convertir a DataFrame (el preprocesador de sklearn lo requiere así)
        input_df = pd.DataFrame([data])
        
        # 3. Transformación: Aplicar la misma limpieza que en el entrenamiento
        # Esto maneja nulos, escala números y codifica categorías automáticamente.
        X_processed = preprocessor.transform(input_df)
        
        # 4. Inferencia
        prediction = model.predict(X_processed)
        
        # 5. Respuesta
        return jsonify({
            'status': 'success',
            'sale_price_prediction': float(prediction[0]),
            'currency': 'USD'
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    # Ejecución en localhost puerto 5000
    app.run(debug=True, port=5000)