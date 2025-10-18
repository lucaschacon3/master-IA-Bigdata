import pandas as pd  # 1) Importamos la librería pandas y le damos el alias 'pd'

# --- 1️⃣ Crear el conjunto de datos ---
data = {  # 2) Diccionario Python con dos listas del mismo tamaño
    'cliente': ['Ana', 'Luis', 'Marta', 'Carlos', 'Sofía', 'Javier', 'Lucía', 'Pedro'],
    'producto': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'A']
}

df = pd.DataFrame(data)  # 3) Convertimos el diccionario a un DataFrame (tabla)
print("=== DataFrame de ejemplo ===")
print(df)                 # 4) Visualizamos la tabla

# --- 2️⃣ Crear los conjuntos de clientes por producto ---
clientes_A = set(df[df['producto'] == 'A']['cliente'])  # 5) Filtramos por producto A y convertimos a conjunto
clientes_B = set(df[df['producto'] == 'B']['cliente'])  # 6) Filtramos por producto B y convertimos a conjunto

print("\nClientes que compraron Producto A:", clientes_A)
print("Clientes que compraron Producto B:", clientes_B)

# --- 3️⃣ Unión: clientes que compraron A o B ---
union_AB = clientes_A.union(clientes_B)  # 7) Unión de conjuntos: A ∪ B
print("\n🔹 Unión (A ∪ B):", union_AB)

# --- 4️⃣ Intersección: clientes que compraron ambos ---
interseccion_AB = clientes_A.intersection(clientes_B)  # 8) Intersección: A ∩ B
print("🔹 Intersección (A ∩ B):", interseccion_AB)

# --- 5️⃣ Diferencia: A - B y B - A ---
solo_A = clientes_A.difference(clientes_B)  # 9) Diferencia: A − B
solo_B = clientes_B.difference(clientes_A)  # 10) Diferencia: B − A
print("🔹 Diferencia A - B:", solo_A)
print("🔹 Diferencia B - A:", solo_B)
