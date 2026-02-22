# entrenar_y_guardar_modelo.py
import joblib
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

print("Cargando MNIST...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data, mnist.target.astype(np.int8)

# Normalizar
X = X / 255.0

# Dividir (opcional, aunque podríamos entrenar con todo)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Entrenando modelo...")
# Usamos una configuración sencilla para que el fichero sea rápido
modelo = MLPClassifier(
    hidden_layer_sizes=(100,),
    activation='relu',
    solver='adam',
    max_iter=20,
    random_state=42
)
modelo.fit(X_train, y_train)

# Evaluación rápida
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Precisión en test: {acc:.4f}")

# Guardar modelo
joblib.dump(modelo, 'modelo_mnist.pkl')
print("Modelo guardado como 'modelo_mnist.pkl'")