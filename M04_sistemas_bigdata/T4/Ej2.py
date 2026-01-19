from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# 1. Inicializar SparkSession
# Usar 'local[*]' para ejecutar en modo local con todos los núcleos disponibles
spark = SparkSession.builder \
    .appName("FiltradoPersonas") \
    .getOrCreate()

# 2. Definir el Esquema (Schema) del DataFrame
schema = StructType([
    StructField("Nombre", StringType(), True),  # Nombre (Tipo String)
    StructField("Edad", IntegerType(), True),   # Edad (Tipo Integer)
    StructField("Peso", IntegerType(), True),   # Peso (Tipo Integer, para filtrado)
    StructField("Talla", IntegerType(), True)  # Talla (Tipo Integer, para filtrado)
])

# 3. Datos de 10 personas ficticias (Peso en kg, Talla en cm)
data = [
    ("Ana", 25, 65, 165),
    ("Luis", 30, 85, 185),
    ("Eva", 22, 75, 168), 
    ("Juan", 40, 72, 175),
    ("Sofia", 28, 58, 170),
    ("Carlos", 35, 90, 190),
    ("Elena", 29, 62, 160),
    ("Miguel", 45, 78, 179),
    ("Paula", 26, 70, 180),
    ("David", 33, 80, 170)
]

# Crear el DataFrame (que actúa como su "tabla" o "base de datos")
df = spark.createDataFrame(data, schema)

# Mostrar el DataFrame completo
print("--- DataFrame Inicial (10 Registros) ---")
df.show()
df.printSchema() # Muestra la definición de los tipos de datos

# 4. Aplicar el filtro: Peso > 70 kg Y Talla < 180 cm
# Usamos el operador lógico AND (&) para combinar las dos condiciones
df_filtrado = df.filter(
    (df.Peso > 70) & (df.Talla < 180)
)

# 5. Mostrar el resultado del filtrado
print("--- Personas con Peso > 70 kg Y Talla < 180 cm ---")
df_filtrado.show()

# 6. Detener la sesión de Spark
spark.stop()