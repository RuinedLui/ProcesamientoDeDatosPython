#iniciamos importando las librerias necesarias
import csv

lista_personas = [] #Lista donde guardaremos los datos diccionarios anidados

#almacenremos los datos csv en una variable
with open('dataset_10000_personas.csv', encoding='utf-8') as datos:
    lector = csv.DictReader(datos)
        #convertimos el lector en una lista para poder recorrerlo   
    p = list(lector)
    
     #iniciamos ciclo for para recorrer cada fila del csv y crear 
     #una estructura de datos basada en diccionarios para cada persona
    for fila in p:
     dato_generales = {
            'id': fila['id'],
            'nombre': fila['nombre'],
            'edad': int(fila['edad']),
            'ciudad': fila['ciudad'],
            'carrera': fila['carrera'],
            'semestre': int(fila['semestre']),
            'promedio': float(fila['promedio']),  
        }
       #ahora estructuramos datos laborales
     dato_laborales = {   
        #cnvertimos el string a booleano comparandolo con 'True'
            'trabajo': fila['trabaja'] == 'True', 
            #ingresos es un float, por lo que convertimos el string a float
            'ingresos': float(fila['ingreso_mensual']),
        }
         #ahora estructuramos dato tecnologicos
     dato_tecnologicos = {
        #convertimos el string a booleano comparandolo con 'True'
                'internet': fila['internet'] == 'True', 
        #convertimos el string a booleano comparandolo con 'True'
                'computadora': fila['computadora'] == 'True', 
         }
         #ahora estructuramos los datos de la persona anidando los diccionarios anteriores
     estudiante_encuestado = {              
            'generales': dato_generales,
            'laborales': dato_laborales,
            'tecnologicos': dato_tecnologicos,
            
         }
     
     lista_personas.append(estudiante_encuestado) #Guardamos el diccionario de estudiante
     #en la lista de personas para su posterior uso en los reportes

     #-----------------INICIO DE LOS REPORTES------------------------------------------

#-------------------------------------REPORTE 13-------------------------------------
#Reporte 13: Ciudad con mayor número de persona (estudiantes)
#contador para almacenar el conteo de personas por ciudad
contador_ciudades = {}

#con ciclo for recorremos cada persona en la lista de personas
for persona in lista_personas:

   #ingresamos laciudad de la persona actual a una variable para facilitar su uso en el contador
    c_actual = persona['generales']['ciudad']

    #si la ciudad ya esta en el contador, incrementamos su conteo
    if c_actual in contador_ciudades:
        #guardamos a la persona en la lista
        contador_ciudades[c_actual].append(persona)
        
    else:
        # INICIALIZAMOS UNA LISTA CON LA PRIMERA PERSONA ENCONTRADA
        contador_ciudades[c_actual] = [persona]
         
#variables para alm acenar la ciudad con mayor numero y
#  variable para almacenar el conteo maximo
ciudad_mayor = ""
conteo_maximo = 0

#recorremos el contador de ciudades para encontrar la ciudad con mayor numero de personas
# USAMOS 'lista_de_personas'
for ciudad, lista_de_personas in contador_ciudades.items():
    
    # CALCULAMOS EL TOTAL
    cantidad = len(lista_de_personas)

   #si el conteo de la ciudad actual es mayor que el conteo 
   # maximo registrado hasta ahora
    if cantidad > conteo_maximo:
        
        #actualizamos el conteo maximo con el conteo de mayor numero
        conteo_maximo = cantidad
        #actualizamos la ciudad con mayor numero a la ciudad
        ciudad_mayor = ciudad

#imprimimos el resultado del reporte
print("-------------------------------------REPORTE 13-------------------------------------")
print(f"Reporte 13: La ciudad con mayor número de personas es {ciudad_mayor}")
print(f"con un total de {conteo_maximo} personas.")

#-------------------------------------REPORTE 14--------------------------------------
#reporte 14: Carrera con mayor promedio de notas
#creamos un diccionario para almacenar la suma de promedios y 
# el conteo de personas por carrera   

contador_promedios = {}

#con ciclo for recorremos cada persona en la lista de personas
for persona in lista_personas:
    #ingresamos la carrera de la persona actual a una variable 
    #para facilitar su uso en el contador
    carrera_actual = persona['generales']['carrera']
    promedio_actual = persona['generales']['promedio']

    #si la carrera ya esta en el contador, actualizamos la suma de promedios y el conteo de personas
    if carrera_actual in contador_promedios:
        #actualizamos la suma de promedios agregando el promedio de la persona actual
        contador_promedios[carrera_actual]['suma'] += promedio_actual
        #agregamos el promedio actual a la lista de notas
        contador_promedios[carrera_actual]['notas'].append(promedio_actual)
        
        #si la carrera no esta en el contador, la agregamos con la suma 
        # inicial del promedio y un conteo inicial de 1
    else:
        # inicializamos la suma de promedios con el promedio de la persona actual
        contador_promedios[carrera_actual] = {'suma': promedio_actual, 'notas': [promedio_actual]}

#variables para almacenar la carrera con mayor promedio y el promedio maximo
carrera_mayor = ""
promedio = 0

#recorremos el contador de promedios para encontrar la carrera con mayor promedio
for carrera, datos in contador_promedios.items():

    #calculamos el promedio de la carrera actual dividiendo
    #  la suma de promedios entre el conteo de personas
    promedio_carrera = datos['suma'] / len(datos['notas'])

    #si el promedio de la carrera actual es mayor que el promedio maximo registrado
    #  hasta ahora
    if promedio_carrera > promedio:
        #actualizamos el promedio maximo con el promedio de la carrera actual
        promedio = promedio_carrera
        #actualizamos la carrera con mayor promedio a la carrera actual
        carrera_mayor = carrera
#imprimimos el resultado del reporte
print("-------------------------------------REPORTE 14-------------------------------------")
print(f"Reporte 14: La carrera con mayor promedio de es {carrera_mayor}")
print(f"con un promedio de:{promedio:.2f}.")

#------------------------REPORTE 15--------------------------------------
#reporte 15:Cantidad de personas sin internet

# creamos una lista vacía para almacenar las personas sin internet 

lista_sin_internet = []

# 2. Con ciclo for recorremos cada persona
for persona in lista_personas:
    
    # 3. Verificamos si la persona no tiene internet usando 
    #if not para evaluar la condición de falta de internet
    if not persona['tecnologicos']['internet']:
      #metemos a la persona a la lista
        lista_sin_internet.append(persona)

# 5 Usamos len() para sacar la cantidad
total_sin_internet = len(lista_sin_internet)

print("-------------------------------------REPORTE 15-------------------------------------")
print(f"Reporte 15: La cantidad de personas sin internet es {total_sin_internet}.")


#-------------------------------------REPORTE 16--------------------------------------
#reporte 16: Relacion entre promedio e ingreso (Analisis por Rango Salarial)
#agrupamos los promedios segun el nivel de ingresos para ver el rendimiento academico

analisis_ingresos = {
    'Ingreso Bajo (0 - 4000)': [],
    'Ingreso Medio (4001 - 7000)': [],
    'Ingreso Alto (Mas de 7000)': []
}

#con ciclo for recorremos cada persona en la lista de personas
for persona in lista_personas:
    #extraemos los datos de tu estructura de diccionarios
    p_promedio = persona['generales']['promedio']
    p_ingreso = persona['laborales']['ingresos']
    
    #clasificamos el promedio del estudiante segun su nivel de ingreso
    if p_ingreso <= 4000:
        analisis_ingresos['Ingreso Bajo (0 - 4000)'].append(p_promedio)
    elif p_ingreso <= 7000:
        analisis_ingresos['Ingreso Medio (4001 - 7000)'].append(p_promedio)
    else:
        analisis_ingresos['Ingreso Alto (Mas de 7000)'].append(p_promedio)

print("-------------------------------------REPORTE 16-------------------------------------")
print("Analisis de Relacion: Rendimiento Academico segun nivel economico")

#recorremos el diccionario usando .items() 
for rango, lista_notas in analisis_ingresos.items():
    
    #sumamos todas las notas del grupo con un ciclo for manual
    suma_notas = 0
    for nota in lista_notas:
    
        suma_notas += nota
    
    #calculamos la cantidad de personas en este rango usando len()
    cantidad_personas = len(lista_notas)
    
    #calculamos el promedio de notas y validamos que la lista no este vacia
    if cantidad_personas > 0:
        promedio_del_grupo = suma_notas / cantidad_personas
    else:
        promedio_del_grupo = 0
        
    # Imprimimos un reporte mas completo que muestra la relacion
    print(f"Grupo {rango}:")
    print(f"  - Cantidad de estudiantes: {cantidad_personas}")
    print(f"  - Promedio academico: {promedio_del_grupo:.2f} ")
    print("-" * 30)

print("------------------------------------------------------------------------------------")