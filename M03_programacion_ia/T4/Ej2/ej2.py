# ==============================================================================
# EJERCICIO 2: Modelado y Evaluación (XGBoost)
# ==============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# --- PREPARACIÓN PREVIA (Viene del Ejercicio 1) ---
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(url).rename(columns={'median_house_value': 'SalePrice'})

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object']).columns

preprocessor = ColumnTransformer(transformers=[
    ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
])

X_prepared = preprocessor.fit_transform(X)

# --- PUNTO 1: Implementa el modelo (XGBoost) ---
X_train, X_test, y_train, y_test = train_test_split(
    X_prepared, y, test_size=0.2, random_state=42
)

# Inicialización de hiperparámetros
model_xgb = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    n_jobs=-1,
    random_state=42
)

# --- PUNTO 2: Entrena el modelo ---
print("Iniciando entrenamiento con XGBoost...")
start_t = time.time()
model_xgb.fit(X_train, y_train)
train_duration = time.time() - start_t

# --- PUNTO 3: Evalúa el modelo ---
y_pred = model_xgb.predict(X_test)

# Métricas
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print(f"\n--- Resultados ---")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: ${rmse:.2f}")
print(f"MAE: ${mae:.2f}")
print(f"Tiempo: {train_duration:.4f}s")

# Validación Cruzada (CV)
print("\nEjecutando Validación Cruzada (K=5)...")
cv_res = cross_val_score(model_xgb, X_prepared, y, scoring="neg_mean_squared_error", cv=5)
print(f"RMSE CV Promedio: ${np.mean(np.sqrt(-cv_res)):.2f}")

# --- PUNTO 4: Análisis de Errores ---
residuals = y_test - y_pred
plt.figure(figsize=(10, 5))
# Versión sin dependencia de statsmodels
sns.residplot(x=y_pred, y=residuals, lowess=False, scatter_kws={'alpha': 0.3})
plt.title("Análisis de Residuos (Predicción vs Error)")
plt.xlabel("Predicciones ($)")
plt.ylabel("Residuos ($)")
plt.savefig("residuals_analysis.png")