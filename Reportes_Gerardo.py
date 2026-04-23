import csv


with open("dataset_10000_personas.csv", 'r', encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    personas = list(reader)

cantidad_personas = len(personas)

# Reporte 1 
print("=" * 45)
print("Reporte 1 - Cantidad de personas por ciudad")
print("=" * 45)

# Contar personas por ciudad 
ciudades = {}

# Se recorre el diccionario para obtener agregar la ciudad o aumentarle la cantidad 
# si ya esta agregado al diccionario

for persona in personas:
    ciudad = persona["ciudad"]
    if ciudad in ciudades:
        ciudades[ciudad] += 1
    else: 
        ciudades[ciudad] = 1

# Se ordenan las ciudades de mayor a menor para tener mas orden 
ciudades_ordenadas = sorted(ciudades.items(), key=lambda x: x[1], reverse=True)

# Mostrar resultados
print(f"{'Ciudad': <20} {'Cantidad': >10} {'Porcentaje':>12}")
print("-" * 45)
# Se recorre el diccionario para obtener las ciudades y la cantidad total y obtener el porcentaje
for ciudad, cantidad in ciudades_ordenadas:
    porcentaje = (cantidad / cantidad_personas) * 100
    print(f"{ciudad:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("-" * 45)
print(f"{'TOTAL':<20} {cantidad_personas:>10} {'100.00%':>12}")

# Reporte 2 
print("=" * 45)
print("Reporte 2 - Cantidad de personas por carrera")
print("=" * 45)

# Contar personas por carrera
carreras = {}

# Se recorre el diccionario para obtener agregar la ciudad o aumentarle la carrera 
# si ya esta agregado al diccionario

for persona in personas:
    carrera = persona["carrera"]
    if carrera in carreras:
        carreras[carrera] += 1
    else: 
        carreras[carrera] = 1

# Se ordenan las carreras de mayor a menor para tener mas orden 
carreras_ordenadas = sorted(carreras.items(), key=lambda x: x[1], reverse=True)

# Mostrar resultados
print(f"{'Carrera': <20} {'Cantidad': >10} {'Porcentaje':>12}")
print("-" * 45)
# Se recorre el diccionario para obtener las ciudades y la cantidad total y obtener el porcentaje
for carrera, cantidad in carreras_ordenadas:
    porcentaje = (cantidad / cantidad_personas) * 100
    print(f"{carrera:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("-" * 45)
print(f"{'TOTAL':<20} {cantidad_personas:>10} {'100.00%':>12}")

# Reporte 3
print("=" * 45)
print("Reporte 3 - Promedio General Académico")
print("=" * 45)

# Diccionario anidado para el cálculo
reporte_promedio = {
    "suma": 0.0,
    "conteo": 0,
    "promedio_final": 0.0
}

for persona in personas:
    # Validación para asegurar que la clave existe
    if "promedio" in persona and persona["promedio"].strip() != "":
        reporte_promedio["suma"] += float(persona["promedio"])
        reporte_promedio["conteo"] += 1

# Calcular promedio solo si hay registros válidos
if reporte_promedio["conteo"] > 0:
    reporte_promedio["promedio_final"] = reporte_promedio["suma"] / reporte_promedio["conteo"]

# Mostrar resultados usando .items()
for clave, valor in reporte_promedio.items():
    if clave == "promedio_final":
        print(f"El promedio general es: {round(valor, 2)}")

print(f"Calculado sobre {reporte_promedio['conteo']} estudiantes válidos")
print("=" * 45)

# Reporte 4
print("=" * 45)
print("Reporte 4 - Promedio Académico por Carrera")
print("=" * 45)

# Contar personas por carrera 
carreras = {}

for persona in personas:
    carrera = persona["carrera"]
    
    # Validación
    if carrera not in carreras:
        carreras[carrera] = {
            "suma": 0.0,
            "conteo": 0,
            "promedio": 0.0
        }
    
    # Validar que el promedio no esté vacío
    if "promedio" in persona and persona["promedio"].strip() != "":
        carreras[carrera]["suma"] += float(persona["promedio"])
        carreras[carrera]["conteo"] += 1

# Calcular promedio por carrera
for carrera, datos in carreras.items():
    if datos["conteo"] > 0:
        datos["promedio"] = datos["suma"] / datos["conteo"]

# Ordenar por promedio de mayor a menor
carreras_ordenadas = sorted(carreras.items(), key=lambda x: x[1]["promedio"], reverse=True)

# Mostrar resultados
print(f"{'Carrera':<25} {'Estudiantes':>12} {'Promedio':>10}")
print("-" * 50)

for carrera, datos in carreras_ordenadas:
    print(f"{carrera:<25} {datos['conteo']:>12} {round(datos['promedio'], 2):>10}")

print("-" * 50)
print(f"Total carreras registradas: {len(carreras.keys())} {'100.00%':>12}")