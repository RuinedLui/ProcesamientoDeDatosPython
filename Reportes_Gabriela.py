import csv

with open("dataset_10000_personas.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    personas = list(reader)

total_registros = len(personas)
print(f"Total de registros cargados: {total_registros}\n")


# Conteo de personas que tienen empleo activo.
# Se itera sobre cada registro del dataset.
print(" REPORTE 5: Cantidad de personas que trabajan ")

conteo_trabajan = 0
for persona in personas:
    # Recorre los campos (campo, valor) de cada persona.
    for campo, valor in persona.items():
        # Si el campo es "trabaja" y su valor es "True", incrementa el contador.
        if campo == "trabaja" and valor == "True":
            conteo_trabajan += 1

no_trabajan = total_registros - conteo_trabajan
print(f"Resultado: {conteo_trabajan} trabajadores / {no_trabajan} desempleados.\n")
print("-------------------------------------------------")


# Cálculo del ingreso promedio sumando todos los ingresos mensuales.
print(" REPORTE 6: Promedio de ingresos mensuales ")

suma_ingresos = 0.0
for persona in personas:
    for campo, valor in persona.items():
        if campo == "ingreso_mensual":
            # Convierte el valor de string a float para realizar operaciones matemáticas.
            suma_ingresos += float(valor)

promedio_ingresos = suma_ingresos / total_registros
print(f"Resultado: El ingreso promedio es de {round(promedio_ingresos, 2)}\n")
print("-------------------------------------------------")


# Conteo de personas que tienen acceso a internet.
print(" REPORTE 7: Cantidad de personas con internet ")

conteo_internet = 0
for persona in personas:
    for campo, valor in persona.items():
        # Si el campo es "internet" y su valor es "True", incrementa el contador.
        if campo == "internet" and valor == "True":
            conteo_internet += 1

sin_internet = total_registros - conteo_internet
print(f"Resultado: {conteo_internet} con acceso / {sin_internet} sin acceso.\n")
print("-------------------------------------------------")


# Conteo de personas que poseen computadora personal.
print(" REPORTE 8: Cantidad de personas con computadora ")

conteo_compu = 0
for persona in personas:
    for campo, valor in persona.items():
        # Si el campo es "computadora" y su valor es "True", incrementa el contador.
        if campo == "computadora" and valor == "True":
            conteo_compu += 1

sin_compu = total_registros - conteo_compu
print(f"Resultado: {conteo_compu} con computadora / {sin_compu} sin computadora.\n")
print("-------------------------------------------------")