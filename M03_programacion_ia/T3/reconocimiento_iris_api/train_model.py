import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Carga de datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

# Entrenamiento
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Guardar modelo y nombres de clases
joblib.dump(model, 'iris_model.pkl')
joblib.dump(iris.target_names, 'class_names.pkl')
print("Modelo guardado exitosamente.")