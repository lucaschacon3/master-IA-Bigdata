# limpiar_ventas_resumen.py
# Requisitos: pandas, numpy, matplotlib, seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- Config ----------------
INPUT = "ventas_con_problemas.csv"   # cambia si tu archivo se llama distinto
OUTPUT_CSV = "ventas_limpias.csv"    # opcional: export del limpio
FIG_BOX = "boxplot_total.png"        # figura de boxplot
PD_OPTIONS = {"display.max_columns": None, "display.width": 120}

for k, v in PD_OPTIONS.items():
    pd.set_option(k, v)

# 1) Carga
df = pd.read_csv(INPUT)

print("\n=== PRIMERAS 5 FILAS ===")
print(df.head())

print("\n=== INFO INICIAL ===")
df.info()

print("\n=== DESCRIBE INICIAL ===")
print(df.describe(include="all"))
print("\n=== VALORES NULOS POR COLUMNA ===")
print(df.isna().sum())

# 2) Conversión de tipos
# fecha → datetime (día/mes primero); numéricos → float/int; strings → str normalizado
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)

# Coerción numérica
for c in ["cantidad", "precio_unitario", "total"]:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# Normalización de texto (strip + lower + colapsar espacios)
def norm_text(s: pd.Series) -> pd.Series:
    s = s.astype("string")
    s = s.str.strip().str.lower()
    s = s.str.replace(r"\s+", " ", regex=True)
    return s

for c in ["tienda", "producto"]:
    if c in df.columns:
        df[c] = norm_text(df[c])

# 3) Métricas de calidad
fechas_invalidas = int(df["fecha"].isna().sum())
duplicados = int(df.duplicated().sum())

print(f"\nFechas inválidas (NaT tras parseo): {fechas_invalidas}")
print(f"Filas duplicadas (exactas): {duplicados}")

# 4) df_limpio = drop_na (después de convertir tipos)
n_original = len(df)
df_limpio = df.dropna().copy()
filas_borradas_por_nulos = n_original - len(df_limpio)

print(f"\nFilas originales: {n_original}")
print(f"Filas después de dropna(): {len(df_limpio)}")
print(f"Filas borradas por nulos: {filas_borradas_por_nulos}")

# 5) Outliers por cuantiles (IQR) en 'total'
# Método IQR: Q1 - 1.5*IQR, Q3 + 1.5*IQR
def iqr_bounds(series: pd.Series, factor=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    return low, high

# Calcular en el DF limpio (sin nulos)
tot = df_limpio["total"].dropna()
if len(tot) > 0:
    low, high = iqr_bounds(tot, factor=1.5)
    mask_out = (tot < low) | (tot > high)
    num_outliers = int(mask_out.sum())
    print(f"\nOutliers en 'total' (IQR 1.5x): {num_outliers}")
    print(f"Limites IQR -> low: {low:.2f}, high: {high:.2f}")
else:
    num_outliers = 0
    low = high = np.nan
    print("\nNo hay datos suficientes en 'total' para calcular outliers.")

# 6) Boxplot de ventas totales (seaborn)
plt.figure(figsize=(6, 5))
sns.boxplot(y=df_limpio["total"], orient="v")
plt.title("Boxplot de ventas totales (total) - Datos limpios")
plt.ylabel("total")
plt.tight_layout()
plt.savefig(FIG_BOX, dpi=120)
plt.close()
print(f"\nBoxplot guardado en: {FIG_BOX}")

# 7) Resumen de datos (describe numérico de limpios + duplicados/fechas/nulos/outliers)
print("\n=== DESCRIBE (DATOS LIMPIOS) ===")
print(df_limpio[["cantidad","precio_unitario","total"]].describe())

print("\n=== RESUMEN ===")
print(f"- Filas originales: {n_original}")
print(f"- Filas tras dropna(): {len(df_limpio)}")
print(f"- Borradas por nulos: {filas_borradas_por_nulos}")
print(f"- Fechas inválidas detectadas: {fechas_invalidas}")
print(f"- Filas duplicadas detectadas (en bruto): {duplicados}")
print(f"- Outliers (IQR 1.5x) en total: {num_outliers}")

# 8) (Opcional) Export CSV limpio
df_limpio.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
print(f"\nCSV limpio exportado a: {OUTPUT_CSV}")
