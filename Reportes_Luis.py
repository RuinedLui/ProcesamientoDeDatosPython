import csv

with open("dataset_10000_personas.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    personas = list(reader)

#Reporte 8: Personas con computadora
reporteComputadoras = {"con_computadora": 0, "sin_computadora": 0}

for persona in personas:
    if persona["computadora"] == "True":
        reporteComputadoras["con_computadora"] += 1
    else:
        reporteComputadoras["sin_computadora"] += 1

for computadora, cantidad in reporteComputadoras.items():
    print(f"Cantidad de personas con {computadora}: {cantidad}")

#Reporte 9: Promedio academico de personas que trabajan
#Reporte 10: Promedio academico de personas que no trabajan
reporte_trabajo = {
    "trabaja":    {"suma": 0, "cantidad": 0},
    "no_trabaja": {"suma": 0, "cantidad": 0}
}

for persona in personas:
    clave = "trabaja" if persona["trabaja"] == "True" else "no_trabaja"
    reporte_trabajo[clave]["suma"] += int(persona["promedio"])
    reporte_trabajo[clave]["cantidad"] += 1

for clave, datos in reporte_trabajo.items():
    promedio = datos["suma"] / datos["cantidad"]
    print(f"Promedio de academico depersonas que {clave}: {promedio:.2f} con {datos['cantidad']} personas")

#Reporte 11: Cantidad de personas por semestre
reporteSemestre = {}

for persona in personas:
    semestre = persona["semestre"]
    if semestre in reporteSemestre:
        reporteSemestre[semestre] += 1
    else:
        reporteSemestre[semestre] = 1

print("Cantidad de personas por semestre:")
for semestre, cantidad in reporteSemestre.items():
    print(f"\tSemestre {semestre}: {cantidad} personas")

#Reporte 12: Edad promedio
reporteEdad = {"suma": 0, "cantidad": 0}

for persona in personas:
    reporteEdad["suma"] += int(persona["edad"])
    reporteEdad["cantidad"] += 1

promedio = reporteEdad["suma"] / reporteEdad["cantidad"]

print("Edad promedio:", round(promedio))
