import csv


with open("dataset_10000_personas.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    personas = list(reader)

total_registros = len(personas)


# ---------------------------------------------------------
# REPORTE 5 – Cantidad de personas que trabajan 
# Lógica: Filtramos por el valor booleano almacenado como texto.
# ---------------------------------------------------------
print("--- REPORTE 5: Cantidad de personas que trabajan ---")
conteo_trabajan = 0
for persona in personas:
    if persona["trabaja"] == "True":
        conteo_trabajan += 1

no_trabajan = total_registros - conteo_trabajan
print(f"Resultado: {conteo_trabajan} trabajadores / {no_trabajan} desempleados.\n")

print("-------------------------------------------------")
# ---------------------------------------------------------
# REPORTE 6 – Promedio de ingresos
# Lógica: Acumulación de valores numéricos (float) para cálculo de media aritmética.
# ---------------------------------------------------------
print("--- REPORTE 6: Promedio de ingresos mensuales ---")
suma_ingresos = 0.0
for persona in personas:
    # Convertimos a float ya que los datos de DictReader son strings por defecto.
    suma_ingresos += float(persona["ingreso_mensual"])

promedio_ingresos = suma_ingresos / total_registros
print(f"Resultado: El ingreso promedio es de Q{round(promedio_ingresos, 2)}\n")

print("-------------------------------------------------")
# ---------------------------------------------------------
# REPORTE 7 – Cantidad de personas con internet  
# Lógica: Cuantificación de penetración de servicios de internet en la muestra.
# ---------------------------------------------------------
print("--- REPORTE 7: Cantidad de personas con internet ---")
conteo_internet = 0
for persona in personas:
    if persona["internet"] == "True":
        conteo_internet += 1

print(f"Resultado: {conteo_internet} con acceso / {total_registros - conteo_internet} sin acceso.\n")

print("-------------------------------------------------")
# ---------------------------------------------------------
# REPORTE 8 – Cantidad de personas con computadora  
# Lógica: Conteo de disponibilidad de hardware (computadora) por persona.
# ---------------------------------------------------------
print("--- REPORTE 8: Cantidad de personas con computadora ---")
conteo_compu = 0
for persona in personas:
    if persona["computadora"] == "True":
        conteo_compu += 1

print(f"Resultado: {conteo_compu} con computadora / {total_registros - conteo_compu} sin computadora.\n")

print("-------------------------------------------------")