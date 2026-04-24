import csv

with open("dataset_10000_personas.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    personas = list(reader)

total_registros = len(personas)
print(f"Total de registros cargados: {total_registros}\n")


# =============================================================
# REPORTE 5 – Cantidad de personas que trabajan
# Usamos .items() para ver todos los campos de cada persona.
# Esto nos permite inspeccionar la fila completa antes de filtrar.
# Lógica: comparamos como string porque DictReader guarda todo como texto.
# =============================================================
print(" REPORTE 5: Cantidad de personas que trabajan ")

conteo_trabajan = 0
for persona in personas:
    # .items() devuelve pares (campo, valor) de cada persona
    # Ejemplo: [("nombre", "Ana"), ("trabaja", "True"), ("ingreso_mensual", "3500.0"), ...]
    for campo, valor in persona.items():
        if campo == "trabaja" and valor == "True":
            conteo_trabajan += 1

no_trabajan = total_registros - conteo_trabajan
print(f"Resultado: {conteo_trabajan} trabajadores / {no_trabajan} desempleados.\n")
print("-------------------------------------------------")


# =============================================================
# REPORTE 6 – Promedio de ingresos mensuales
# Usamos .items() para localizar el campo "ingreso_mensual".
# Convertimos a float porque todos los valores del CSV son strings.
# Lógica: suma acumulada / total = media aritmética.
# =============================================================
print(" REPORTE 6: Promedio de ingresos mensuales ")

suma_ingresos = 0.0
for persona in personas:
    for campo, valor in persona.items():
        if campo == "ingreso_mensual":
            # float() convierte el string "3500.0" → 3500.0 (número decimal)
            suma_ingresos += float(valor)

promedio_ingresos = suma_ingresos / total_registros
print(f"Resultado: El ingreso promedio es de {round(promedio_ingresos, 2)}\n")
print("-------------------------------------------------")


# =============================================================
# REPORTE 7 – Cantidad de personas con acceso a internet
# Usamos .items() para recorrer los campos de cada persona.
# Medimos la penetración del servicio de internet en la muestra.
# =============================================================
print(" REPORTE 7: Cantidad de personas con internet ")

conteo_internet = 0
for persona in personas:
    for campo, valor in persona.items():
        if campo == "internet" and valor == "True":
            conteo_internet += 1

sin_internet = total_registros - conteo_internet
print(f"Resultado: {conteo_internet} con acceso / {sin_internet} sin acceso.\n")
print("-------------------------------------------------")


# =============================================================
# REPORTE 8 – Cantidad de personas con computadora
# Mismo patrón que los reportes 5 y 7.
# .items() nos permite ser explícitos sobre QUÉ campo estamos leyendo.
# =============================================================
print(" REPORTE 8: Cantidad de personas con computadora ")

conteo_compu = 0
for persona in personas:
    for campo, valor in persona.items():
        if campo == "computadora" and valor == "True":
            conteo_compu += 1

sin_compu = total_registros - conteo_compu
print(f"Resultado: {conteo_compu} con computadora / {sin_compu} sin computadora.\n")
print("-------------------------------------------------")