from collections import defaultdict

# Documentos de prueba
documentos = [
    "la computacion distribuida es potente",
    "la computacion paralela es rapida",
    "distribuida y paralela son paradigmas diferentes"
]

# 1. FASE MAP
def fase_map(docs):
    pares_kv = []
    for doc in docs:
        palabras = doc.lower().split()
        for palabra in palabras:
            pares_kv.append((palabra, 1))
    return pares_kv

# 2. FASE SHUFFLE AND SORT
def fase_shuffle_sort(pares_kv):
    agrupados = defaultdict(list)
    for clave, valor in pares_kv:
        agrupados[clave].append(valor)
    return sorted(agrupados.items())

# 3. FASE REDUCE
def fase_reduce(datos_agrupados):
    resultado = {}
    for clave, valores in datos_agrupados:
        resultado[clave] = sum(valores)
    return resultado

# Ejecución del programa
mapeo = fase_map(documentos)
agrupado = fase_shuffle_sort(mapeo)
conteo_final = fase_reduce(agrupado)

# Resultado
for palabra, total in conteo_final.items():
    print(f"'{palabra}': {total}")