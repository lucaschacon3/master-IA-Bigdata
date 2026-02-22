# predecir_imagen.py
import joblib
import numpy as np
from PIL import Image
import sys
import os

def preprocesar_imagen(ruta_imagen):
    """
    Carga una imagen, la convierte a 28x28 en escala de grises,
    normaliza y aplana.
    Devuelve un array de forma (1, 784) listo para el modelo.
    """
    try:
        # Abrir imagen
        img = Image.open(ruta_imagen)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None

    # Convertir a escala de grises
    img = img.convert('L')
    
    # Redimensionar a 28x28 (MNIST size)
    img = img.resize((28, 28), Image.Resampling.LANCZOS)
    
    # Convertir a numpy array
    img_array = np.array(img, dtype=np.float32)
    
    # Opcional: invertir si el fondo es blanco y el dígito negro
    # Para decidir, podemos mirar el promedio: si es >127, probablemente fondo blanco
    if np.mean(img_array) > 127:
        img_array = 255 - img_array
    
    # Normalizar a [0, 1]
    img_array = img_array / 255.0
    
    # Aplanar a vector de 784
    img_vector = img_array.reshape(1, -1)
    
    return img_vector

def main():
    # Verificar argumento
    if len(sys.argv) < 2:
        print("Uso: python predecir_imagen.py <ruta_de_la_imagen>")
        print("Ejemplo: python predecir_imagen.py mi_digito.png")
        return
    
    ruta = sys.argv[1]
    
    # Comprobar que el archivo existe
    if not os.path.exists(ruta):
        print(f"El archivo '{ruta}' no existe.")
        return
    
    # Cargar modelo
    try:
        modelo = joblib.load('modelo_mnist.pkl')
    except FileNotFoundError:
        print("No se encontró el archivo 'modelo_mnist.pkl'.")
        print("Ejecuta primero 'entrenar_y_guardar_modelo.py' para generarlo.")
        return
    
    # Preprocesar imagen
    X = preprocesar_imagen(ruta)
    if X is None:
        return
    
    # Predecir
    prediccion = modelo.predict(X)[0]
    probabilidades = modelo.predict_proba(X)[0]
    
    print(f"\n🔢 El modelo predice que el dígito es: **{prediccion}**")
    print("\n📊 Probabilidades por dígito:")
    for i, prob in enumerate(probabilidades):
        print(f"   {i}: {prob:.4f}")

if __name__ == "__main__":
    main()