def sistema_experto(hechos: dict) -> list[str]:
    conclusiones = []

    if hechos.get("vibracion_alta") and hechos.get("temperatura_alta"):
        conclusiones.append("Posible fallo en el rodamiento.")

    if hechos.get("presion_baja") and hechos.get("caudal_bajo"):
        conclusiones.append("Revisar la bomba.")

    if hechos.get("aceite_bajo") and hechos.get("ruido_metalico"):
        conclusiones.append("Parada inmediata: revisar lubricación y componentes internos.")
       
    if hechos.get("consumo_elevado") and not hechos.get("aumento_carga", False):
        conclusiones.append("Posible desgaste interno o pérdidas mecánicas.")

    if hechos.get("motor_parado") and not hechos.get("error_electrico", False):
        conclusiones.append("Comprobar posible bloqueo mecánico.")

    if not conclusiones:
        conclusiones.append("Sin diagnóstico claro con las reglas actuales.")

    return conclusiones

hechos_1 = {
    "vibracion_alta": True,
    "temperatura_alta": True,
    "presion_baja": False,
    "caudal_bajo": False,
    "aceite_bajo": False,
    "ruido_metalico": False,
    "consumo_elevado": False,
    "aumento_carga": False,
    "motor_parado": False,
    "error_electrico": False,
}
print("Caso 1:", sistema_experto(hechos_1))

hechos_2 = {
    "vibracion_alta": False,
    "temperatura_alta": False,
    "presion_baja": True,
    "caudal_bajo": True,
    "aceite_bajo": False,
    "ruido_metalico": False,
    "consumo_elevado": False,
    "aumento_carga": False,
    "motor_parado": False,
    "error_electrico": False,
    }
print("Caso 2:", sistema_experto(hechos_2))

hechos_3 = {
    "vibracion_alta": False,
    "temperatura_alta": False,
    "presion_baja": False,
    "caudal_bajo": False,
    "aceite_bajo": False,
    "ruido_metalico": False,
    "consumo_elevado": False,
    "aumento_carga": False,
    "motor_parado": True,
    "error_electrico": False,
    }
print("Caso 3:", sistema_experto(hechos_3))
