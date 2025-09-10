#ACTIVIDAD 1

lista_multiplo_4 =list(range(4,101,4))
print(lista_multiplo_4)

#ACTIVIDAD 2 

mi_lista = ["musica", "futbol", "juegos", "automobilismo", "viajes"]
print("El penultimo elemento de mi lista es:",mi_lista[-2])

#ACTIVIDAD 3

palabras = []
palabras.append("UTN")
palabras.append("programacion")
palabras.append("Desarrollo")
print(palabras)

#ACTIVIDAD 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#ACTIVIDAD 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#ACTIVIDAD 6

lista_num = list(range(10,31,5))
print("Los dos primero elementos son ",lista_num[:2])

#ACTIVIDAD 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "falcon"
autos[2] = "bora"
print(autos)

#ACTIVIDAD 8

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#ACTIVIDAD 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#ACTIVIDAD 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)