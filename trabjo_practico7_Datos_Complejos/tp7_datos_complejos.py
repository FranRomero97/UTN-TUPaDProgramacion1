#ACTIVIDAD 1 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

print(precios_frutas)

#ACTIVIDAD 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

print(precios_frutas)

precios_frutas['Banana'] = 1300
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#ACTIVIDA 3

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

print(precios_frutas)

precios_frutas['Banana'] = 1300
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

frutas = sorted(precios_frutas.keys())

print(frutas)

#ACTVIDAD 4

agenda = {}

print("Carga de 5 contactos")
for i in range (5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el numero del contacto {nombre}: ")
    agenda[nombre] = numero

consulta = input("\Ingrese el nombre del contacto a buscar")

if consulta in agenda:
    print(f"El numero de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontro ningun contanto con ese nombre {consulta}")

#ACTIVIDAD 5 

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

print("\nPalabras unicas: ")
print(palabras_unicas)

contador = {}
for palabra in palabras:
    print(palabra)
    if palabra in contador:
        contador[palabra] += 1
    else:        
        contador[palabra] = 1

print("\nCantidad de veces que aprece cada palabra: ")
print(contador)

#ACTIVIDA 6

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print("El promedio de", nombre, "es:", promedio)

#ACTIVIDAD 7

print("Ingrese los nombres de los estudiantes que aprobaron el Parcial 1.")
print("Escriba 'fin' para terminar la lista.\n")

parcial1 = set()
while True:
    nombre = input("Nombre: ")
    if nombre.lower() == "fin":
        break
    parcial1.add(nombre)

print("\nIngrese los nombres de los estudiantes que aprobaron el Parcial 2.")
print("Escriba 'fin' para terminar la lista.\n")

parcial2 = set()
while True:
    nombre = input("Nombre: ")
    if nombre.lower() == "fin":
        break
    parcial2.add(nombre)

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("\n--- RESULTADOS ---")
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#ACTIVIDAD 8

productos = {}

while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para salir): ")
    if producto.lower() == "fin":
        break
    if producto in productos:
        opcion = input("El producto existe. Desea agregar unidades? (s/n): ")
        if opcion.lower() == "s":
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            productos[producto] += cantidad
    else:
        opcion = input("El producto no existe. Desea agregarlo? (s/n): ")
        if opcion.lower() == "s":
            cantidad = int(input("Ingrese el stock inicial: "))
            productos[producto] = cantidad

consulta = input("Ingrese el producto que desea consultar: ")
if consulta in productos:
    print("Stock de", consulta, ":", productos[consulta])
else:
    print("El producto no existe en el inventario.")

#ACTIVIDAD 9

agenda = {}

while True:
    Dia = input("Ingrese el día (o 'fin' para salir): ")
    if Dia.lower() == "fin":
        break
    hora = input("Ingrese la hora: ")
    evento = input("Ingrese el evento: ")
    agenda[(Dia, hora)] = evento

dia_consulta = input("Ingrese el día que desea consultar: ")
hora_consulta = input("Ingrese la hora que desea consultar: ")

if (dia_consulta, hora_consulta) in agenda:
    print("Evento:", agenda[(dia_consulta, hora_consulta)])
else:
    print("No hay eventos en ese día y hora.")

#ACTIVIDAD 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print(invertido)

