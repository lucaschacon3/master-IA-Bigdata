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
    (1, "MapReduce divide grandes tareas en subtareas para procesamiento distribuido."),
    (2, "La velocidad es clave en Big Data para el análisis en tiempo real."),
    (3, "PySpark es la API de Python para usar las capacidades de procesamiento en memoria de Spark."),
    (4, "HDFS es el sistema de archivos distribuido de Hadoop que almacena bloques de Big Data."),
    (5, "El beneficio de Spark sobre Hadoop es su velocidad gracias al procesamiento en memoria."),
    (6, "La función Map de MapReduce genera pares clave-valor."),
    (7, "PySpark permite el análisis distribuido y es muy usado en Machine Learning (MLlib)."),
    (8, "MapReduce consta de las fases Map, Shuffle and Sort, y Reduce."),
    (9, "Los RDDs son la unidad básica de datos en Spark y son inmutables."),
    (10, "La variedad de datos requiere herramientas especializadas de Big Data.")
]

df = spark.createDataFrame(data, schema)

print("--- DataFrame Inicial ---")
df.show(truncate=False)

# --- 2. FASE MAP: Preparación y Expansión de Palabras ---

# 2.1 Limpiar y tokenizar:
#   a) Convertir a minúsculas (lower)
#   b) Eliminar puntuación (regexp_replace)
#   c) Dividir la frase en palabras (split)

df_palabras_limpias = df.select(
    explode(
        split(
            regexp_replace(lower(col("Frase")), "[^a-z\\s]", ""), # Eliminar caracteres no deseados
            " "
        )
    ).alias("Palabra")
)

# 2.2 Eliminar celdas vacías que pueden aparecer al limpiar y dividir
df_palabras_limpias = df_palabras_limpias.filter(col("Palabra") != "")

print("\n--- Resultado de la Fase MAP (Palabras expandidas) ---")
df_palabras_limpias.show(10, truncate=False) # Muestra las primeras 10 palabras expandidas

# --- 3. FASE SHUFFLE & REDUCE: Agrupación y Conteo ---

# 3.1 Agrupación (Simula Shuffle & Sort): Agrupar por la clave 'Palabra'
# 3.2 Reducción (Simula Reduce): Contar las ocurrencias de cada grupo

df_word_count = df_palabras_limpias.groupBy("Palabra").count()


# --- 4. Mostrar el Resultado Final ---
print("\n--- Conteo Final de Palabras (Word Count) ---")
df_word_count.orderBy(col("count").desc()).show(truncate=False)

# 5. Detener la sesión de Spark
spark.stop()