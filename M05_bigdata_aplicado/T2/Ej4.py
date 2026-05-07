import time

class NodoDistribuido:
    def __init__(self, id):
        self.id = id
        self.datos = {}
        self.activo = True

    def guardar(self, clave, valor):
        if self.activo:
            self.datos[clave] = valor
            return True
        return False

    def obtener(self, clave):
        if self.activo:
            return self.datos.get(clave)
        return None

class SistemaAlmacenamiento:
    def __init__(self, num_nodos=3):
        self.nodos = [NodoDistribuido(i) for i in range(num_nodos)]

    def almacenar_dato(self, clave, valor):
        print(f"Intentando replicar '{clave}': '{valor}' en todos los nodos...")
        for nodo in self.nodos:
            if nodo.guardar(clave, valor):
                print(f"  > Guardado en Nodo {nodo.id}")
            else:
                print(f"  > Nodo {nodo.id} caído. No se pudo guardar aquí.")

    def recuperar_dato(self, clave):
        for nodo in self.nodos:
            valor = nodo.obtener(clave)
            if valor is not None:
                print(f"Dato recuperado del Nodo {nodo.id}")
                return valor
        print("Error: El dato no está disponible en ningún nodo activo.")
        return None

    def simular_fallo(self, id_nodo):
        self.nodos[id_nodo].activo = False
        print(f"\n!!! FALLO CRÍTICO: El Nodo {id_nodo} se ha desconectado !!!\n")

    def recuperar_nodo(self, id_nodo):
        self.nodos[id_nodo].activo = True
        print(f"--- Nodo {id_nodo} restaurado y en línea ---\n")

# --- EJECUCIÓN DEL SISTEMA ---

sistema = SistemaAlmacenamiento(3)

# 1. Almacenamiento inicial (Replicación)
sistema.almacenar_dato("usuario_101", "Juan Perez")
sistema.almacenar_dato("usuario_102", "Maria Garcia")

# 2. Simulación de fallo
sistema.simular_fallo(0) # Cae el nodo 0

# 3. Prueba de operatividad (Tolerancia a fallos)
print("Consulta tras el fallo:")
dato = sistema.recuperar_dato("usuario_101")
print(f"Resultado: {dato}")

# 4. Recuperación del nodo y acceso a datos
sistema.recuperar_nodo(0)
print(f"Consulta en nodo recuperado: {sistema.nodos[0].obtener('usuario_101')}")