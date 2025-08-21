#ACTIVIDAD 1
print("Hola Mundo") 


#ACTIVIDAD 2
nombre = str (input("ingrese su nombre")) 
print(f"hola {nombre}.")

#ACTIVIDAD 3
nombre = str (input("Ingrese su nombre")) 

apellido = str (input("Ingrese su apellido"))

edad = int (input("Ingrese su Edad"))

residencia = str (input("Ingrese su lugar de residencia"))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#ACTIVIDAD 4
import math 
radio = float(input("Ingrese el radio del circulo que desea calcular: "))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio
print(f"el area es: {area:.2f}")
print(f"el perimetro es: {perimetro:.2f}")   

#ACTIVIDAD 5
seg = float(input("Ingrese una cantidad de seg: ")) 
horas = seg / 3600
print (f"{seg} Equivalen a {horas:.2f} horas.")

#ACTIVIDAD 6
num = int(input("Ingrese el numero del cual desea su tabla de Multiplicar: ")) 
print(f"\n La tabla de multiplicar del{num}:\n")
for i in range (1,11):
    print (f"{num} x {i} = {num * i}")


 #ACTIVIDAD 7

num1 = int(input("Ingrese un numero (distinto de 0) :"))
num2 = int(input("Ingrese un numero (distinto de 0):"))

if num1 == 0 or num2 == 0:
    print("ERROR los numeros ingresados deben de ser distintos de 0")


else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 


print(f"\nResultados con {num1} y {num2}")
print(f"suma: {suma}")
print(f"resta: {resta}")
print(f"multiplicacion: {multiplicacion}")
print(f"division: {division:.2f}:")


#ACTIVIDAD 8 

altura = float(input("Ingrese su altura"))
peso = float(input("Ingrese su peso"))
masa_corp = peso / altura
print(f"Su indice de masa corporal es: {masa_corp:.2f}.")

#ACTIVIDAD 9

temp = float(input("Ingrese una temperatura en celsius: "))
fahrenheit = 9 / 5 * temp + 32 
print(fahrenheit)

#ACTIVIDAD 10

num1 = int(input("Ingrese el primero numero: " ))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

pro = num1 + num2 + num3
promedio = pro / 3


print(f"El promedio de los numeros ingresados es: {promedio}")