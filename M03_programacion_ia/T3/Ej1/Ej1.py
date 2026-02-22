import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')  # Ignorar warnings de convergencia (por simplicidad)

# 1. Cargar MNIST
print("Cargando MNIST...")
mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
X, y = mnist.data, mnist.target.astype(np.int8)  # y viene como string, convertir a int

# 2. Preprocesamiento: normalizar y aplanar (ya está aplanado, 784 columnas)
X = X / 255.0  # normalizar a [0,1]

# 3. División en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Tamaño de entrenamiento: {X_train.shape[0]} muestras")
print(f"Tamaño de prueba: {X_test.shape[0]} muestras")

# 4. Definir algunas configuraciones de hiperparámetros para probar
#    Vamos a probar manualmente tres configuraciones diferentes

configuraciones = [
    {
        'name': 'Una capa oculta 100 neuronas',
        'hidden_layer_sizes': (100,),
        'activation': 'relu',
        'solver': 'adam',
        'max_iter': 20,
        'random_state': 42
    },
    {
        'name': 'Dos capas ocultas (100,50) con tanh',
        'hidden_layer_sizes': (100, 50),
        'activation': 'tanh',
        'solver': 'sgd',
        'learning_rate_init': 0.01,
        'max_iter': 30,
        'random_state': 42
    },
    {
        'name': 'Una capa 50 neuronas con logistic',
        'hidden_layer_sizes': (50,),
        'activation': 'logistic',
        'solver': 'adam',
        'max_iter': 25,
        'random_state': 42
    }
]

# 5. Entrenar y evaluar cada configuración
resultados = []

for config in configuraciones:
    print(f"\n--- Entrenando: {config['name']} ---")
    # Crear modelo con los hiperparámetros (excluyendo 'name')
    params = {k: v for k, v in config.items() if k != 'name'}
    mlp = MLPClassifier(**params)
    
    # Entrenar
    mlp.fit(X_train, y_train)
    
    # Predecir
    y_pred = mlp.predict(X_test)
    
    # Métricas
    acc = accuracy_score(y_test, y_pred)
    resultados.append({
        'name': config['name'],
        'accuracy': acc,
        'model': mlp
    })
    print(f"Exactitud en test: {acc:.4f}")

# 6. Mostrar resumen de resultados
print("\n=== Resumen de exactitudes ===")
for r in resultados:
    print(f"{r['name']}: {r['accuracy']:.4f}")

# 7. Para la mejor configuración, mostrar matriz de confusión y reporte
mejor = max(resultados, key=lambda x: x['accuracy'])
print(f"\n=== Mejor modelo: {mejor['name']} ===")
y_pred_mejor = mejor['model'].predict(X_test)

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred_mejor)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Matriz de Confusión - {mejor["name"]}')
plt.xlabel('Predicho')
plt.ylabel('Real')
plt.savefig("matriz")
plt.show()

# Reporte de clasificación
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred_mejor))

# Opcional: Mostrar algunas predicciones con imágenes
fig, axes = plt.subplots(2, 5, figsize=(10,5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_test[i].reshape(28,28), cmap='gray')
    ax.set_title(f'Real: {y_test[i]}\nPred: {y_pred_mejor[i]}')
    ax.axis('off')
plt.tight_layout()
plt.savefig("ejemplo")
plt.show()