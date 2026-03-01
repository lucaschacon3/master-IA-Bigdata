# --------------------------------------
# --- PUNTO 1: Importa las librerías ---
# --------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Configuración de visualización
sns.set_theme(style="whitegrid")


# --------------------------------
# --- PUNTO 2: Carga los datos ---
# --------------------------------

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
df = pd.read_csv(url)

# Renombramos el target para que se llame como dice el ejercicio
df = df.rename(columns={'median_house_value': 'SalePrice'})

print(f"Estructura del dataset: {df.shape}")

# --------------------------------------
# --- PUNTO 3: Análisis Exploratorio ---
# --------------------------------------

# Punto 3.1: Estadística descriptiva
print("\n--- Estadística Descriptiva ---")
print(df.describe().T)

# Punto 3.2: Visualización
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
sns.histplot(df['SalePrice'], kde=True, color='blue')
plt.title('Distribución de SalePrice (Target)')

plt.subplot(2, 2, 2)
sns.boxplot(x=df['SalePrice'], color='red')
plt.title('Detección de Outliers en SalePrice')

plt.subplot(2, 2, 3)
sns.scatterplot(data=df, x='median_income', y='SalePrice', alpha=0.3)
plt.title('Relación: Ingreso Medio vs SalePrice')

plt.subplot(2, 2, 4)
sns.countplot(data=df, y='ocean_proximity')
plt.title('Distribución de Proximidad al Océano')
plt.tight_layout()
plt.savefig("eda_plots.png")

# Punto 3.3: Análisis de correlación
print("\n--- Matriz de Correlación con el Target ---")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix['SalePrice'].sort_values(ascending=False))


# ------------------------------------------------------------
# --- PASOS ADICIONALES: Preprocesamiento con Scikit-Learn ---
# ------------------------------------------------------------
# Separamos el target de las variables predictoras
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

# Definimos qué columnas son numéricas y cuáles categóricas
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object']).columns

# Creamos los Transformers (Punto de rigor técnico)
# 1. Para números: Imputamos nulos con la mediana y escalamos (StandardScaler)
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# 2. Para categorías: OneHotEncoding (convierte texto a columnas numéricas 0/1)
cat_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Unimos ambos procesos en un ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, num_cols),
        ('cat', cat_transformer, cat_cols)
    ]
)

# Ejecutamos el preprocesamiento
X_prepared = preprocessor.fit_transform(X)

print("\n--- Resumen de Preprocesamiento ---")
print(f"Nuevas dimensiones de X (tras One-Hot): {X_prepared.shape}")
print("Tratamiento de nulos y escalado completado.")