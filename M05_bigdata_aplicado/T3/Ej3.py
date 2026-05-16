import hashlib

def calcular_hash(ruta_archivo, algoritmo):
    if algoritmo.upper() == 'MD5':
        hasher = hashlib.md5()
    elif algoritmo.upper() == 'SHA-256' or algoritmo.upper() == 'SHA256':
        hasher = hashlib.sha256()
    else:
        return "Error: Algoritmo no soportado."

    try:
        with open(ruta_archivo, 'rb') as archivo:
            # Lectura en bloques por rendimiento (Big Data)
            for bloque in iter(lambda: archivo.read(4096), b""):
                hasher.update(bloque)
        return hasher.hexdigest()
    except FileNotFoundError:
        return "Error: El archivo no existe."

def verificar_integridad(hash_calculado, hash_esperado):
    if hash_calculado.lower() == hash_esperado.lower():
        return "✅ INTEGRIDAD CONFIRMADA: Los hashes coinciden."
    else:
        return "❌ ADVERTENCIA: Los hashes NO coinciden. El archivo ha sido modificado."

# --- Ejecución del programa ---
if __name__ == "__main__":
    archivo = 'uber.csv'  # Asegúrate de tener el uber.csv en la misma ruta
    algo = 'SHA-256'

    print("\n" + "-"*60)
    print(" 1: CÁLCULO DEL HASH")
    print("-" * 60)
    hash_resultante = calcular_hash(archivo, algo)
    print(f"Archivo analizado: {archivo}")
    print(f"Algoritmo empleado: {algo}")
    print(f"Hash generado: {hash_resultante}")

    print("\n" + "-"*60)
    print(" 2: VALIDACIÓN DE INTEGRIDAD")
    print("-" * 60)
    print("Caso A: Comparación con el hash original (Sin modificar)")
    print(verificar_integridad(hash_resultante, hash_resultante))

    print("\nCaso B: Comparación con un hash distinto (Archivo alterado)")
    hash_falso = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    print(verificar_integridad(hash_resultante, hash_falso))
    print("-" * 60 + "\n")