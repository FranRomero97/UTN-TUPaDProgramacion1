#ACTIVIDAD 1

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

#ACTIVIDAD 2

def saludar_usuario(nombre):
    return "Hola "+ nombre + "!"

nombre_usuario: str = str(input("Ingrese su nombre: "))
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#ACTIVIDAD 3 

def informacion_personal(nombre, apellido, edad, residencia):
    return "Soy "+ nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + residencia 

nombre_usuario: str = str(input("Ingrese su nombre: "))
apellido__usuario: str = str(input("Ingrese su apellido "))
edad_usuario: int = int(input("Ingrese su edad "))
residencia_usuario: str = str(input("Ingrese su lugar de residencia "))

saludo = informacion_personal(nombre_usuario, apellido__usuario, edad_usuario, residencia_usuario)
print(saludo)

#ACTIVIDAD 4

import math 

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcula_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio 
    return perimetro

radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcula_perimetro_circulo(radio)

print("El area del circulo es: ",area)
print("El perimetro del circulo es: ",perimetro)

#ACTIVIDAD 5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print("La cantidad de segundos ingrasdos equivalen a ",horas, "horas")

#ACTIVIDAD 6

def tabla_multiplicar(numero):

    print("La tabla de multiplicar del numero: " , numero)
    for i in range (1 , 11):
        resultado = numero * i
        print(numero,"x", i , "=" , resultado)

numero = int(input("Ingrese el numero que quiere multiplicar: "))

tabla_multiplicar(numero)

#ACTIVIDAD 7
def operaciones_basicas(a , b):
    suma = a + b
    resta = a - b 
    multiplicar = a * b

    if b != 0:
        division = a / b
    else:
        division = "no se puede dividir por 0"
    
    return (suma , resta , division , multiplicar)

a = float(input("Ingrese el primer numero: "))

b = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a , b)

print("Los resultado son")

print("Suma: ",resultados[0])
print("resta: ",resultados[1])
print("division: ",resultados[2])
print("multiplicacion: ", resultados[3])

#ACTIVIDAD 8

def calcula_imc(peso , altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en KG: "))

altura = float(input("Ingrese su altura en Metros: "))

resultado = calcula_imc(peso ,  altura)

print("Su indice de masa corporal es de: ", round(resultado , 2))

#ACTIVIDAD 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius} °C equivalen a {resultado} °F ")

#ACTIVIDAD 10

def calcular_promedio(a , b , c):
    promedio = (a + b + c) / 3
    return promedio 

num1 = float(input("Ingrese la primer nota: "))

num2 = float(input("Ingrese la segunda nota nota: "))

num3 = float(input("Ingrese la tercer nota: "))

resultado = calcular_promedio(num1 , num2 , num3)

print("El promedio de las notas es: ", round(resultado , 2))