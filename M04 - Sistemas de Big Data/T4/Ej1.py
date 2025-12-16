import pandas as pd
import polars as pl
import requests
import time

# 1. Descargar y preparar los datos una sola vez

datos_pandas= pd.read_csv("organizations-2000000.csv")
df_pandas=pd.DataFrame(datos_pandas)

print(f"Total de registros: {len(df_pandas)}")

# --- 2. Pandas: Carga y Medición ---
inicio_pandas = time.time()
# Operación: Filtrar por 'origin_country'
resultado_pandas = df_pandas[df_pandas['Country'] == "Spain"]
fin_pandas = time.time()
tiempo_pandas = fin_pandas - inicio_pandas
print(f"\nPandas finalizado. Registros: {len(resultado_pandas)}")
print(f"Tiempo Pandas: {tiempo_pandas:.6f} segundos")


# --- 3. Polars: Carga y Medición ---
datos_polars = pl.read_csv("organizations-2000000.csv")
df_polars = pl.DataFrame(datos_polars)

inicio_polars = time.time()
resultado_polars = df_polars.filter(pl.col('Country') == "Spain")
fin_polars = time.time()
tiempo_polars = fin_polars - inicio_polars
print(f"\nPolars finalizado. Registros: {len(resultado_polars)}")
print(f"Tiempo Polars: {tiempo_polars:.6f} segundos")


if tiempo_pandas < tiempo_polars:
    print(f"\nPandas fue más rápido por {tiempo_polars - tiempo_pandas:.6f} segundos.")
elif tiempo_polars < tiempo_pandas:
    print(f"\nPolars fue más rápido por {tiempo_pandas - tiempo_polars:.6f} segundos.")