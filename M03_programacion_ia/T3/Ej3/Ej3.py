import os
# Evita que tensorflow busque la GPU Y choque con los DRIVERS
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf
from tensorflow.keras import layers, models, Input
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

# 1. CARGA
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 2. PREPROCESADO
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# 3. ARQUITECTURA (Sintaxis Keras 3 limpia)
model = models.Sequential([
    Input(shape=(28, 28, 1)), 
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# 4. COMPILACIÓN
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. ENTRENAMIENTO
print("Entrenando en CPU para evitar conflictos de drivers...")
model.fit(x_train, y_train, epochs=3, validation_split=0.1)

# 6. EVALUACIÓN Y MATRIZ
y_pred = np.argmax(model.predict(x_test), axis=1)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title('Matriz de Confusión - Keras (CPU)')
plt.savefig('resultado_keras.png')
print("Proceso finalizado. Imagen guardada como 'resultado_keras.png'")