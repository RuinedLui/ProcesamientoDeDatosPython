import csv


with open("encuesta_comida_rapida.csv", 'r', encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    encuestados = list(reader)

cantidad_total = len(encuestados)

# ============================================================
# Reporte 1 - Cantidad de personas por comida preferida
# ============================================================
print("=" * 50)
print("Reporte 1 - Comida rápida preferida")
print("=" * 50)

comidas = {}

for encuestado in encuestados:
    comida = encuestado["comida"]
    if comida in comidas:
        comidas[comida] += 1
    else:
        comidas[comida] = 1

comidas_ordenadas = sorted(comidas.items(), key=lambda x: x[1], reverse=True)

print(f"{'Comida':<20} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 45)

for comida, cantidad in comidas_ordenadas:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{comida:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("-" * 45)
print(f"{'TOTAL':<20} {cantidad_total:>10} {'100.00%':>12}")

# ============================================================
# Reporte 2 - Cantidad de personas por frecuencia de consumo
# ============================================================
print("=" * 50)
print("Reporte 2 - Frecuencia de consumo")
print("=" * 50)

frecuencias = {}

for encuestado in encuestados:
    frecuencia = encuestado["frecuencia"]
    if frecuencia in frecuencias:
        frecuencias[frecuencia] += 1
    else:
        frecuencias[frecuencia] = 1

frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

print(f"{'Frecuencia':<20} {'Cantidad':>10} {'Porcentaje':>12}")
print("-" * 45)

for frecuencia, cantidad in frecuencias_ordenadas:
    porcentaje = (cantidad / cantidad_total) * 100
    print(f"{frecuencia:<20} {cantidad:>10} {porcentaje:>11.2f}%")

print("-" * 45)
print(f"{'TOTAL':<20} {cantidad_total:>10} {'100.00%':>12}")

# ============================================================
# Reporte 3 - Promedio general de satisfacción (producto, servicio y general)
# ============================================================
print("=" * 50)
print("Reporte 3 - Promedio General de Satisfacción")
print("=" * 50)

reporte_promedio = {
    "producto": {"suma": 0.0, "conteo": 0, "promedio": 0.0},
    "servicio": {"suma": 0.0, "conteo": 0, "promedio": 0.0},
    "general":  {"suma": 0.0, "conteo": 0, "promedio": 0.0},
}

for encuestado in encuestados:
    for campo in ["producto", "servicio", "general"]:
        if campo in encuestado and encuestado[campo].strip() != "":
            reporte_promedio[campo]["suma"] += float(encuestado[campo])
            reporte_promedio[campo]["conteo"] += 1

for campo, datos in reporte_promedio.items():
    if datos["conteo"] > 0:
        datos["promedio"] = datos["suma"] / datos["conteo"]

print(f"{'Indicador':<25} {'Encuestados':>12} {'Promedio':>10}")
print("-" * 50)

etiquetas = {
    "producto": "Satisfacción producto",
    "servicio": "Satisfacción servicio",
    "general":  "Calificación general"
}

for campo, datos in reporte_promedio.items():
    print(f"{etiquetas[campo]:<25} {datos['conteo']:>12} {round(datos['promedio'], 2):>10}")

print("=" * 50)

# ============================================================
# Reporte 4 - Promedio de satisfacción por comida preferida
# ============================================================
print("=" * 50)
print("Reporte 4 - Satisfacción promedio por comida")
print("=" * 50)

por_comida = {}

for encuestado in encuestados:
    comida = encuestado["comida"]

    if comida not in por_comida:
        por_comida[comida] = {
            "suma_producto":      0.0,
            "suma_servicio":      0.0,
            "suma_recomendacion": 0.0,
            "suma_general":       0.0,
            "conteo":             0
        }

    if encuestado.get("producto", "").strip() != "":
        por_comida[comida]["suma_producto"]      += float(encuestado["producto"])
        por_comida[comida]["suma_servicio"]      += float(encuestado["servicio"])
        por_comida[comida]["suma_recomendacion"] += float(encuestado["recomendacion"])
        por_comida[comida]["suma_general"]       += float(encuestado["general"])
        por_comida[comida]["conteo"]             += 1

# Calcular promedios por comida
resultados = []
for comida, datos in por_comida.items():
    if datos["conteo"] > 0:
        n = datos["conteo"]
        resultados.append({
            "comida":        comida,
            "conteo":        n,
            "prom_producto": round(datos["suma_producto"]      / n, 2),
            "prom_servicio": round(datos["suma_servicio"]      / n, 2),
            "prom_rec":      round(datos["suma_recomendacion"] / n, 2),
            "prom_general":  round(datos["suma_general"]       / n, 2),
        })

# Ordenar por calificación general de mayor a menor
resultados_ordenados = sorted(resultados, key=lambda x: x["prom_general"], reverse=True)

print(f"{'Comida':<18} {'N':>5} {'Producto':>9} {'Servicio':>9} {'Rec.':>6} {'General':>8}")
print("-" * 58)

for r in resultados_ordenados:
    print(
        f"{r['comida']:<18} {r['conteo']:>5} "
        f"{r['prom_producto']:>9} {r['prom_servicio']:>9} "
        f"{r['prom_rec']:>6} {r['prom_general']:>8}"
    )

print("-" * 58)
print(f"Total comidas registradas: {len(resultados_ordenados)}")
print("=" * 50)