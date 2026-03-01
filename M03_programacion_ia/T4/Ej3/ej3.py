# ==============================================================================
# EJERCICIO 3: Optimización y Despliegue
# ==============================================================================

import pandas as pd
import numpy as np
import joblib
import time
from xgboost import XGBRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- RECONSTRUCCIÓN DEL ESTADO (Punto crítico para nuevo fichero) ---
def prepare_data():
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
    df = pd.read_csv(url).rename(columns={'median_house_value': 'SalePrice'})
    
    X = df.drop("SalePrice", axis=1)
    y = df["SalePrice"]
    
    num_cols = X.select_dtypes(include=[np.number]).columns
    cat_cols = X.select_dtypes(exclude=[np.number]).columns
    
    preprocessor = ColumnTransformer(transformers=[
        ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sca', StandardScaler())]), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ])
    
    X_prepared = preprocessor.fit_transform(X)
    return train_test_split(X_prepared, y, test_size=0.2, random_state=42), preprocessor

(X_train, X_test, y_train, y_test), preprocessor = prepare_data()

# --- 1. AJUSTE DE HIPERPARÁMETROS (GridSearch) ---
print("--- Iniciando Optimización de XGBoost ---")
param_grid = {
    'max_depth': [4, 5],
    'learning_rate': [0.05],
    'n_estimators': [500],
    'reg_lambda': [2, 5, 10] # Diferentes niveles de regularización L2
}

grid_xgb = GridSearchCV(XGBRegressor(random_state=42), param_grid, cv=3, scoring='r2', n_jobs=-1)
grid_xgb.fit(X_train, y_train)
best_xgb = grid_xgb.best_estimator_

print(f"Mejores parámetros: {grid_xgb.best_params_}")
print(f"R² XGBoost Optimizado: {r2_score(y_test, best_xgb.predict(X_test)):.4f}")

# --- 2. PRUEBA CON OTROS MODELOS (Red Neuronal MLP) ---
print("\n--- Entrenando Red Neuronal (MLP) ---")
mlp = MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
start_mlp = time.time()
mlp.fit(X_train, y_train)
mlp_time = time.time() - start_mlp

print(f"R² Red Neuronal: {r2_score(y_test, mlp.predict(X_test)):.4f} | Tiempo: {mlp_time:.2f}s")

# --- 4. DESPLIEGUE (Guardado de artefactos) ---
joblib.dump(best_xgb, 'modelo_final.pkl')
joblib.dump(preprocessor, 'preprocesador.pkl')
print("\nArtefactos guardados con éxito para la API.")