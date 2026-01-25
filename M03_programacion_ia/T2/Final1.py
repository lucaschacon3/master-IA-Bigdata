from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargamos los datos
iris = load_iris()
# Creamos un DataFrame para que sea legible
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("Primeras filas del dataset:")
print(df.head())

X = iris.data
Y = iris.target

# Dividimos: 80% para entrenar, 20% para probar
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

scaler = StandardScaler()
# Ajustamos solo con los datos de entrenamiento para evitar fuga de información
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Instanciamos con k=5
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, Y_train)

# Predicción
y_pred = knn5.predict(X_test)

print(f"Accuracy (k=5): {accuracy_score(Y_test, y_pred):.2f}")
print("Matriz de Confusión:")
print(confusion_matrix(Y_test, y_pred))


for k in [1, 15]:
    modelo = KNeighborsClassifier(n_neighbors=k)
    modelo.fit(X_train, Y_train)
    pred = modelo.predict(X_test)
    print(f"Resultado con k={k}: Accuracy = {accuracy_score(Y_test, pred):.2f}")