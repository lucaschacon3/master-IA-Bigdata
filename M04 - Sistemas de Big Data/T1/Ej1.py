import pandas as pd

# Ahora algunos estudiantes cursan ambas asignaturas
data = {
    "estudiante": ["Ana", "Ana", "Luis", "María", "María", "Carlos", "Lucía", "Javier", "Sara"],
    "asignatura": ["Matemáticas", "Historia", "Historia", "Matemáticas", "Historia", "Historia", "Matemáticas", "Matemáticas", "Historia"]
}

# Convertimos a DataFrame
df = pd.DataFrame(data)

print("=== Datos iniciales ===")
print(df)

# Listas de estudiantes por asignatura
matematicas = set(df[df["asignatura"] == "Matemáticas"]["estudiante"])
historia = set(df[df["asignatura"] == "Historia"]["estudiante"])

# 1. Unión: estudiantes que cursan Matemáticas o Historia
union = matematicas.union(historia)

# 2. Intersección: estudiantes que cursan ambas asignaturas
interseccion = matematicas.intersection(historia)

# 3. Diferencia:
solo_matematicas = matematicas.difference(historia)
solo_historia = historia.difference(matematicas)

print("\n=== Resultados ===")
print(f"Estudiantes que cursan Matemáticas o Historia: {union}")
print(f"Estudiantes que cursan ambas asignaturas: {interseccion}")
print(f"Estudiantes que cursan solo Matemáticas: {solo_matematicas}")
print(f"Estudiantes que cursan solo Historia: {solo_historia}")
