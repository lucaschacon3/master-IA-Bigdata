import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar el dataset
df = pd.read_csv('uber.csv')

print("\n" + "-"*60)
print("ESTADO INICIAL: SHAPE Y NULOS (Para comparar)")
print("-" * 60)
print("Shape inicial:", df.shape)
print("\nNulos iniciales:\n", df.isnull().sum())

# ---------------------------------------------------------
# 1. Identificar y eliminar filas duplicadas
# ---------------------------------------------------------
df = df.drop_duplicates()

print("\n" + "-"*60)
print("1: ELIMINAR DUPLICADOS")
print("-" * 60)
print("Shape tras eliminar duplicados:", df.shape)

# ---------------------------------------------------------
# 2. Comprobar la integridad de los datos
# ---------------------------------------------------------
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')

if 'fare_amount' in df.columns:
    df = df[df['fare_amount'] > 0]

if 'key' in df.columns:
    df['key'] = df['key'].astype(str)
    df = df[df['key'].str.strip() != '']

print("\n" + "-"*60)
print("2: INTEGRIDAD DE DATOS")
print("-" * 60)
print("Tipos de datos actuales:\n", df.dtypes)
if 'fare_amount' in df.columns:
    print("\nComprobación de precios <= 0 (debe estar vacío):")
    print(df[df['fare_amount'] <= 0])

# ---------------------------------------------------------
# 3. Reemplazar valores nulos o inválidos
# ---------------------------------------------------------
df = df.dropna(subset=['pickup_datetime', 'key'] if set(['pickup_datetime', 'key']).issubset(df.columns) else [])

if 'fare_amount' in df.columns:
    df['fare_amount'] = df['fare_amount'].fillna(df['fare_amount'].median())

print("\n" + "-"*60)
print("3: NULOS TRAS LIMPIEZA")
print("-" * 60)
print(df.isnull().sum())

# ---------------------------------------------------------
# 4. Normalizar o estandarizar columnas numéricas
# ---------------------------------------------------------
scaler = StandardScaler()
# Usamos passenger_count porque no hay columna distance
cols_to_scale = ['fare_amount', 'passenger_count'] 
cols_to_scale = [col for col in cols_to_scale if col in df.columns]

if cols_to_scale:
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

print("\n" + "-"*60)
print("4: DATOS ESTANDARIZADOS")
print("-" * 60)
if cols_to_scale:
    print(df[cols_to_scale].head())