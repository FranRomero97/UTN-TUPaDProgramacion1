#ACTIVIDAD 1

edad_usuario : int = int(input("ingrese su edad"))

mayor : str = "Es mayor de edad" if edad_usuario > 18 else "Es menor"

print (mayor)
     
ingrese su edad18
Es menor

#ACTIVIDAD 2

nota_alumno : float = float(input("ingrese nota"))

calificacion = "Aprobado" if nota_alumno >= 6 else "Desaprobado"

print (calificacion)
     
ingrese nota5
Desaprobado

#ACTIVIDAD 3

numero:float = float(input("ingrese un numero"))

if (numero % 2 == 0):
    print("Ha ingresado un numero par")

else:
    print("Por favor, ingrese un numero par")
     
ingrese un numero2
Ha ingresado un numero par

#ACTIVIDAD 4

edad:int = int(input("ingrese su edad"))

if (edad >=0 and edad < 12):
    print("Niño/a")

elif (edad >= 12 and edad < 18):
    print("Adolescente")

elif (edad >= 18 and edad < 30):
    print("Adulto/a joven")

elif (edad >= 30 and edad < 100):
    print("Adulto/a")

else: print("Ingrese una edad valida")
     
ingrese su edad101
Ingrese una edad valida

#ACTIVIDAD 5

contraseña: str  = str(input("Ingrese la contraseña"))

if (len(contraseña) >= 8 and len(contraseña) <=14 ):
    print("Contraseña valida")

else: print("Por favor, ingrese una contraseña entre 8 y 14")
     
Ingrese la contraseña1234567
Por favor, ingrese una contraseña entre 8 y 14

#ACTIVIDAD 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"moda={moda}, mediana={mediana}, media={media}")

if (moda == mediana and moda == media):
    print("Sin sesgo")

elif (media > mediana and mediana > moda):
    print("Sesgo positivo o a la derecha")

elif (media < mediana and mediana < moda):
    print("Sesgo negativo o a la izquierda")

     
moda=20, mediana=20, media=20
Sin sesgo

#ACTIVIDAD 7

frase : str = str(input("Ingrese una frase: "))

ult = frase[len(frase)-1].lower()

if( ult in "aeiou"):
   print(f"{frase}!")
else:
   print(frase)

     
Ingrese una frase: asdadasdxx
asdadasdxx

#ACTIVIDAD 8

nombre : str = str(input("Ingrese su nombre: "))
print("1: Nombre en Mayus\n2: Nombre en Minus\n3: Primer letra mayus")
opcion : int = int(input("Ingrese opcion: "))
def casos (arg):
  if arg == 1:
    print(nombre.upper())

  elif arg == 2:
    print(nombre.lower())

  elif arg == 3:
    print(nombre.title())
  else:
    print("opcion no valida")

casos(opcion)

#ACTIVIDAD 9

magnitud : float = float(input("ingrese magniutud del terremoto"))

if (magnitud > 3) :
    print ("Muy leve")

elif (magnitud >=3 and magnitud < 4):
    print ("Leve")

elif (magnitud >= 4 and magnitud < 5):
    print("Moderado")

elif (magnitud >= 5 and magnitud < 6):
    print("Fuerte")

elif (magnitud >= 6 and magnitud < 7):
    print("Muy Fuerte")

elif (magnitud >= 7):
    print("Extremo")

else:
    print ("Colocar valor correcto")