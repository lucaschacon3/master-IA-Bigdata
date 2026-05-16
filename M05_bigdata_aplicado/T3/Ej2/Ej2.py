import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# Cargar el dataset (asumiendo que ya está limpio del Ejercicio 1, aquí lo cargamos crudo para el ejemplo)
df = pd.read_csv('uber.csv')

# ---------------------------------------------------------
# 1. Extraer nueva información (Feature Engineering)
# ---------------------------------------------------------
# A. Extraer datos temporales
if 'pickup_datetime' in df.columns:
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
    df['hour'] = df['pickup_datetime'].dt.hour
    df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df['month'] = df['pickup_datetime'].dt.month

# B. Calcular la distancia real usando la fórmula de Haversine (Matemática esférica)
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radio de la Tierra en km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

if set(['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']).issubset(df.columns):
    df['distance_km'] = haversine_distance(df['pickup_latitude'], df['pickup_longitude'],
                                           df['dropoff_latitude'], df['dropoff_longitude'])

print("\n" + "-"*60)
print(" 1: EXTRACCIÓN DE NUEVA INFORMACIÓN (FEATURE ENGINEERING)")
print("-" * 60)
print(df[['pickup_datetime', 'hour', 'distance_km']].head())

# ---------------------------------------------------------
# 2. Análisis Estadístico y Detección de Outliers
# ---------------------------------------------------------
print("\n" + "-"*60)
print(" 2: DETECCIÓN ESTADÍSTICA DE OUTLIERS")
print("-" * 60)
# Mostramos estadísticas descriptivas de precio y distancia
if set(['fare_amount', 'distance_km']).issubset(df.columns):
    print(df[['fare_amount', 'distance_km']].describe())

# ---------------------------------------------------------
# 3. Pandas Profiling (Generación del Reporte)
# ---------------------------------------------------------
print("\n" + "-"*60)
print("CAPTURA 3: GENERACIÓN DEL REPORTE PROFILING")
print("-" * 60)
print("Generando reporte HTML... (Esto puede tardar unos minutos)")
print("Abre el archivo 'uber_report.html' en tu navegador cuando termine.")

# Se genera el reporte ignorando las variables de coordenadas para no saturar
profile = ProfileReport(df.drop(columns=['key', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude'], errors='ignore'), 
                        title="Uber Dataset Profiling Report", 
                        explorative=True)
profile.to_file("uber_report.html")