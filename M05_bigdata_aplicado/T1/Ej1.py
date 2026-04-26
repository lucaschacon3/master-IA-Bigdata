
import time
import pandas as pd
import polars as pl
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, stddev, to_timestamp

# Los archivos extraídos se llaman 'rating.csv' y 'movie.csv'
file_ratings = "rating.csv"
file_movies = "movie.csv"

print("\n--- INICIANDO COMPARATIVA ---")

# --- 1. PANDAS ---
start_pd = time.time()
pd_ratings = pd.read_csv(file_ratings)
pd_movies = pd.read_csv(file_movies)
df_pd = pd_ratings.merge(pd_movies, on='movieId')

df_pd['date'] = pd.to_datetime(df_pd['timestamp']) 
action_pd = df_pd[(df_pd['genres'].str.contains('Action', na=False)) & (df_pd['rating'] >= 4)]
stats_pd = df_pd.groupby('userId')['rating'].agg(['mean', 'std'])
avg_pd = df_pd.groupby('movieId')['rating'].mean().sort_values(ascending=False)
time_pd = time.time() - start_pd
print(f"Pandas: {time_pd:.2f} s")

# --- 2. POLARS (EAGER) ---
start_pl_eager = time.time()
pl_ratings = pl.read_csv(file_ratings)
pl_movies = pl.read_csv(file_movies)
df_pl = pl_ratings.join(pl_movies, on='movieId')

df_pl = df_pl.with_columns(pl.col("timestamp").str.to_datetime("%Y-%m-%d %H:%M:%S").alias("date"))
action_pl = df_pl.filter((pl.col("genres").str.contains("Action")) & (pl.col("rating") >= 4))
stats_pl = df_pl.group_by("userId").agg([pl.col("rating").mean().alias("mean"), pl.col("rating").std().alias("std")])
avg_pl = df_pl.group_by("movieId").agg(pl.col("rating").mean()).sort("rating", descending=True)
time_pl_eager = time.time() - start_pl_eager
print(f"Polars Eager: {time_pl_eager:.2f} s")

# --- 3. POLARS (LAZY) ---
start_pl_lazy = time.time()
q_ratings = pl.scan_csv(file_ratings)
q_movies = pl.scan_csv(file_movies)


q_pl = q_ratings.join(q_movies, on='movieId').with_columns(pl.col("timestamp").str.to_datetime("%Y-%m-%d %H:%M:%S").alias("date"))

action_lazy_q = q_pl.filter((pl.col("genres").str.contains("Action")) & (pl.col("rating") >= 4))
stats_lazy_q = q_pl.group_by("userId").agg([pl.col("rating").mean().alias("mean"), pl.col("rating").std().alias("std")])
avg_lazy_q = q_pl.group_by("movieId").agg(pl.col("rating").mean()).sort("rating", descending=True)

action_lazy = action_lazy_q.collect()
stats_lazy = stats_lazy_q.collect()
avg_lazy = avg_lazy_q.collect()
time_pl_lazy = time.time() - start_pl_lazy
print(f"Polars Lazy: {time_pl_lazy:.2f} s")

# --- 4. PYSPARK (LOCAL) ---
spark = SparkSession.builder.appName("Benchmark").master("local[*]").getOrCreate()

start_spark = time.time()
sp_ratings = spark.read.csv(file_ratings, header=True, inferSchema=True)
sp_movies = spark.read.csv(file_movies, header=True, inferSchema=True)
df_sp = sp_ratings.join(sp_movies, "movieId")

df_sp = df_sp.withColumn("date", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"))
action_sp = df_sp.filter(col("genres").contains("Action") & (col("rating") >= 4))
stats_sp = df_sp.groupBy("userId").agg(mean("rating").alias("mean"), stddev("rating").alias("std"))
avg_sp = df_sp.groupBy("movieId").agg(mean("rating").alias("avg_rating")).orderBy(col("avg_rating").desc())

action_sp.count()
stats_sp.count()
avg_sp.count()
time_spark = time.time() - start_spark
print(f"PySpark Local: {time_spark:.2f} s")

spark.stop()