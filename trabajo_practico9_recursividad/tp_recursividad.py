#ACTIVIDAD 1 

def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

while True:
    entrada_usuario = input("Ingrese un número entero positivo para calcular factoriales hasta él: ")
    
    if not entrada_usuario.isdigit():
        print("Entrada no válida. Por favor, ingrese un número entero.")
        continue
        
    numero_usuario = int(entrada_usuario)
    
    if numero_usuario < 1:
        print("Por favor, ingrese un número entero positivo (mayor o igual a 1).")
        continue
    else:
        break

i = 1
while i <= numero_usuario:
    resultado = factorial_recursivo(i)
    print(f"El factorial de {i} es: {resultado}")
    i += 1

print("-----------------")

#ACTIVIDAD 2

def fibonacci_recursivo(posicion):
    if posicion <= 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)


while True:
    entrada_limite = input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci (entero no negativo): ")
    
    if entrada_limite.startswith('-'):
        print("Por favor, ingrese una posición no negativa.")
        continue
    
    if not entrada_limite.isdigit():
        print("Entrada no válida. Por favor, ingrese un número entero.")
        continue

    limite_usuario = int(entrada_limite)
    
    if limite_usuario < 0:
        print("Por favor, ingrese una posición no negativa.") 
        continue
    else:
        break

i = 0
serie_fib = []
while i <= limite_usuario:
    serie_fib.append(fibonacci_recursivo(i))
    i += 1
    
print(f"La serie de Fibonacci hasta la posición {limite_usuario} es:")
print(serie_fib)


print("-----------------")

#ACTIVIDAD 3

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)


while True:
    entrada_base = input("Ingrese la base (un número entero): ")
    es_entero = True
    if entrada_base.startswith('-'):
        temp_base = entrada_base[1:]
    else:
        temp_base = entrada_base
        
    if not temp_base.isdigit():
        print("Entrada de base no válida. Por favor, ingrese un número entero.")
        continue
    
    base = int(entrada_base)
    break

while True:
    entrada_exponente = input("Ingrese el exponente (un número entero no negativo): ")
    
    if entrada_exponente.startswith('-'):
        print("Esta función solo está diseñada para exponentes no negativos.")
        continue
        
    if not entrada_exponente.isdigit():
        print("Entrada de exponente no válida. Por favor, ingrese un número entero.")
        continue
    
    exponente = int(entrada_exponente)
    
    if exponente < 0:
        print("Esta función solo está diseñada para exponentes no negativos.")
        continue
    else:
        break

resultado_potencia = potencia_recursiva(base, exponente)
print(f"El resultado de {base}^{exponente} es: {resultado_potencia}")

print("-----------------")

#ACTIVIDAD 4

def decimal_a_binario_recursivo(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

while True:
    entrada_decimal = input("Ingrese un número entero positivo para convertir a binario: ")

    if entrada_decimal.startswith('-'):
        print("Por favor, ingrese un número entero positivo.")
        continue
        
    if not entrada_decimal.isdigit():
        print("Entrada no válida. Por favor, ingrese un número entero positivo.")
        continue

    num_decimal = int(entrada_decimal)

    if num_decimal < 0:
        print("Por favor, ingrese un número entero positivo.")
        continue
    else:
        break

if num_decimal == 0:
    print("El número 0 en binario es: 0")
else:
    binario = decimal_a_binario_recursivo(num_decimal)
    print(f"El número {num_decimal} en binario es: {binario}")

print("-----------------")

#ACTIVIDAD 5

def es_palindromo_recursiva(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo_recursiva(palabra[1:-1])
    else:
        return False
palindromo = input("ingrese palabra para ver si es o no es palindromo: ")
if es_palindromo_recursiva(palindromo) == True:
    print(f"{palindromo} si es un palindromo")
else:
    print(f"{palindromo} no es un palindromo")

print("-----------------")

#ACTIVIDAD 6

def suma_digitos_recursiva(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos_recursiva(n // 10)

while True:
    n = input("ingrese un numero para sumar sus digitos ")
    if n.isdigit():
        n = int(n)
        suma_digitos_recursiva(n)
        break
    else:
        print("error ingrese numeros del (0-9)")

print("-----------------")

#ACTIVIDAD 7

def contar_bloques_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques_recursiva(n - 1)

while True:
    bloques = input("ingrese cantidad de bloques ")
    if bloques.isdigit():
        bloques = int(bloques)
        contar_bloques_recursiva(bloques)
        break
    else:
        print("error ingrese numeros del (0-9)")

print("-----------------")

#ACTIVIDAD 8

def contar_digito_recursiva(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10
    
    apariciones = 0
    
    if ultimo_digito == digito:
        apariciones = 1
    
    return apariciones + contar_digito_recursiva(numero // 10, digito)


while True:
    num = input("ingrese numero entero positivo ")
    if num.isdigit():
        num = int(num)
        digito = input("ingrese un digito del (0-9)")
        if digito.isdigit():
            digito = int(digito)
            if len(digito) > 1:
                print("error debe ser solo un digito")
            else:
                contar_digito_recursiva(num, digito)
                break
        else:
            print("error ingrese un numero del (0-9)")
    else:
        print("error ingrese numeros del (0-9)")