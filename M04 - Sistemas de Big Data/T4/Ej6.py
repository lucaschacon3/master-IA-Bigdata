from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import explode, split, lower, regexp_replace, col

# --- 1. Inicialización y DataFrame (Tu código original) ---
spark = SparkSession.builder \
    .appName("FrasesBigData") \
    .getOrCreate()


schema = StructType([
    StructField("ID", IntegerType(), True),
    StructField("Frase", StringType(), True)
])

data = [
    (1, "MapReduce divide grandes tareas en subtareas para procesamiento distribuido"),
    (2, "La velocidad es clave en Big Data para el análisis en tiempo real"),
    (3, "PySpark es la API de Python para usar las capacidades de procesamiento en memoria de Spark"),
    (4, "HDFS es el sistema de archivos distribuido de Hadoop que almacena bloques de Big Data"),
    (5, "El beneficio de Spark sobre Hadoop es su velocidad gracias al procesamiento en memoria"),
    (6, "La función Map de MapReduce genera pares clave-valor."),
    (7, "PySpark permite el análisis distribuido y es muy usado en Machine Learning (MLlib)"),
    (8, "MapReduce consta de las fases Map, Shuffle and Sort, y Reduce"),
    (9, "Los RDDs son la unidad básica de datos en Spark y son inmutables"),
    (10, "La variedad de datos requiere herramientas especializadas de Big Data")
]

df = spark.createDataFrame(data, schema)

print("--- DataFrame Inicial ---")
df.show(truncate=False)

# --- 2. FASE MAP: Preparación y Expansión de Palabras ---
df_palabras_limpias = df.select(
    explode(
        split(lower(col("Frase")), " ")
    ).alias("Palabra")
)

df_palabras_limpias = df_palabras_limpias.filter(col("Palabra") != "")
print("\n--- Resultado de la Fase MAP (Palabras expandidas) ---")
df_palabras_limpias.show(10, truncate=False)


# --- 3. FASE REDUCE: Conteo de Palabras ---
df_word_count = df_palabras_limpias.groupBy("Palabra").count()
print("\n--- Conteo Final de Palabras (Word Count) ---")
df_word_count.orderBy(col("count").desc()).show()


spark.stop()