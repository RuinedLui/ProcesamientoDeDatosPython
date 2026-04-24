import csv

# =============================================================================
# 1. CARGA Y PREPARACIÓN DE DATOS
# =============================================================================
# Se abre el archivo una sola vez para alimentar todos los reportes
with open("dataset_10000_personas.csv", 'r', encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    personas = list(reader)

cantidad_personas = len(personas)
total_registros = cantidad_personas

# Estructura de diccionarios anidados (Requerida específicamente por Edwin)
lista_personas = []
for fila in personas:
    estudiante_encuestado = {
        'generales': {
            'id': fila['id'],
            'nombre': fila['nombre'],
            'edad': int(fila['edad']),
            'ciudad': fila['ciudad'],
            'carrera': fila['carrera'],
            'semestre': int(fila['semestre']),
            'promedio': float(fila['promedio'])
        },
        'laborales': {
            'trabajo': fila['trabaja'] == 'True',
            'ingresos': float(fila['ingreso_mensual'])
        },
        'tecnologicos': {
            'internet': fila['internet'] == 'True',
            'computadora': fila['computadora'] == 'True'
        }
    }
    lista_personas.append(estudiante_encuestado)

# =============================================================================
# 2. REPORTES DE GERARDO (1 - 4)
# =============================================================================
print("=" * 45)
print("REPORTE 1 - Cantidad de personas por ciudad")
print("=" * 45)
ciudades = {}
for persona in personas:
    ciudad = persona["ciudad"]
    ciudades[ciudad] = ciudades.get(ciudad, 0) + 1

ciudades_ordenadas = sorted(ciudades.items(), key=lambda x: x[1], reverse=True)
print(f"{'Ciudad': <20} {'Cantidad': >10} {'Porcentaje':>12}")
print("-" * 45)
for ciudad, cantidad in ciudades_ordenadas:
    porcentaje = (cantidad / cantidad_personas) * 100
    print(f"{ciudad:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("\n" + "=" * 45)
print("REPORTE 2 - Cantidad de personas por carrera")
print("=" * 45)
carreras_g = {}
for persona in personas:
    carrera = persona["carrera"]
    carreras_g[carrera] = carreras_g.get(carrera, 0) + 1

carreras_ord = sorted(carreras_g.items(), key=lambda x: x[1], reverse=True)
print(f"{'Carrera': <20} {'Cantidad': >10} {'Porcentaje':>12}")
print("-" * 45)
for carrera, cantidad in carreras_ord:
    porcentaje = (cantidad / cantidad_personas) * 100
    print(f"{carrera:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("\n" + "=" * 45)
print("REPORTE 3 - Promedio General Académico")
print("=" * 45)
suma_p = sum(float(p["promedio"]) for p in personas if p["promedio"].strip() != "")
print(f"El promedio general es: {round(suma_p / cantidad_personas, 2)}")

print("\n" + "=" * 45)
print("REPORTE 4 - Promedio Académico por Carrera")
print("=" * 45)
carreras_prom = {}
for persona in personas:
    carrera = persona["carrera"]
    if carrera not in carreras_prom:
        carreras_prom[carrera] = {"suma": 0.0, "conteo": 0}
    carreras_prom[carrera]["suma"] += float(persona["promedio"])
    carreras_prom[carrera]["conteo"] += 1

print(f"{'Carrera':<25} {'Estudiantes':>12} {'Promedio':>10}")
print("-" * 50)
for carrera, datos in sorted(carreras_prom.items(), key=lambda x: x[1]["suma"]/x[1]["conteo"], reverse=True):
    prom = datos["suma"] / datos["conteo"]
    print(f"{carrera:<25} {datos['conteo']:>12} {round(prom, 2):>10}")

# =============================================================================
# 3. REPORTES DE GABRIELA (5 - 8)
# =============================================================================
print("\n" + "-" * 50)
print("REPORTE 5: Personas que trabajan")
c_trabajan = sum(1 for p in personas if p["trabaja"] == "True")
print(f"Resultado: {c_trabajan} trabajadores / {total_registros - c_trabajan} desempleados.")

print("\nREPORTE 6: Promedio de ingresos")
s_ingresos = sum(float(p["ingreso_mensual"]) for p in personas)
print(f"Resultado: El ingreso promedio es de Q{round(s_ingresos / total_registros, 2)}")

print("\nREPORTE 7: Personas con internet")
c_net = sum(1 for p in personas if p["internet"] == "True")
print(f"Resultado: {c_net} con acceso / {total_registros - c_net} sin acceso.")

print("\nREPORTE 8: Personas con computadora")
c_compu = sum(1 for p in personas if p["computadora"] == "True")
print(f"Resultado: {c_compu} con computadora / {total_registros - c_compu} sin computadora.")

# =============================================================================
# 4. REPORTES DE LUIS (9 - 12)
# =============================================================================
print("\n" + "-" * 50)
print("REPORTE 9 y 10: Promedio académico según trabajo")
rep_trabajo = {"trabaja": {"s": 0.0, "c": 0}, "no_trabaja": {"s": 0.0, "c": 0}}
for p in personas:
    k = "trabaja" if p["trabaja"] == "True" else "no_trabaja"
    rep_trabajo[k]["s"] += float(p["promedio"])
    rep_trabajo[k]["c"] += 1
for k, v in rep_trabajo.items():
    print(f"Promedio de personas que {k}: {v['s']/v['c']:.2f}")

print("\nREPORTE 11: Cantidad por semestre")
rep_sem = {}
for p in personas:
    s = p["semestre"]
    rep_sem[s] = rep_sem.get(s, 0) + 1
for sem, cant in sorted(rep_sem.items(), key=lambda x: int(x[0])):
    print(f"\tSemestre {sem}: {cant} personas")

print("\nREPORTE 12: Edad promedio")
s_edad = sum(int(p["edad"]) for p in personas)
print(f"Edad promedio: {round(s_edad / total_registros)}")

# =============================================================================
# 5. REPORTES DE EDWIN (13 - 16)
# =============================================================================
print("\n" + "-" * 50)
print("REPORTE 13: Ciudad con mayor población")
cont_ciudades = {}
for p in lista_personas:
    ciu = p['generales']['ciudad']
    if ciu not in cont_ciudades: cont_ciudades[ciu] = []
    cont_ciudades[ciu].append(p)
ciu_max = max(cont_ciudades, key=lambda k: len(cont_ciudades[k]))
print(f"La ciudad con más personas es {ciu_max} con {len(cont_ciudades[ciu_max])}.")

print("\nREPORTE 14: Carrera con mayor promedio")
cont_prom = {}
for p in lista_personas:
    car = p['generales']['carrera']
    if car not in cont_prom: cont_prom[car] = []
    cont_prom[car].append(p['generales']['promedio'])
car_max = max(cont_prom, key=lambda k: sum(cont_prom[k])/len(cont_prom[k]))
print(f"Carrera líder: {car_max} (Promedio: {sum(cont_prom[car_max])/len(cont_prom[car_max]):.2f})")

print("\nREPORTE 15: Personas sin internet")
sin_net = sum(1 for p in lista_personas if not p['tecnologicos']['internet'])
print(f"Total sin internet: {sin_net}")

print("\nREPORTE 16: Análisis de Rendimiento por Rango Salarial")
analisis = {'Ingreso Bajo (0-4k)': [], 'Ingreso Medio (4k-7k)': [], 'Ingreso Alto (>7k)': []}
for p in lista_personas:
    ing, pr = p['laborales']['ingresos'], p['generales']['promedio']
    if ing <= 4000: analisis['Ingreso Bajo (0-4k)'].append(pr)
    elif ing <= 7000: analisis['Ingreso Medio (4k-7k)'].append(pr)
    else: analisis['Ingreso Alto (>7k)'].append(pr)

for rango, notas in analisis.items():
    p_grupo = sum(notas)/len(notas) if notas else 0
    print(f"Grupo {rango}: Cantidad {len(notas)}, Promedio {p_grupo:.2f}")
print("-" * 50)