#ejercicio-1

for numero in range(0,101):
    print("Numero ", numero)
    

#ejercicio-2 

numero = int(input("Ingresá un número entero: "))

# Aseguramos que el número sea positivo para contar dígitos
numero_absoluto = abs(numero)

# Inicializamos contador
cantidad_digitos = 0

# Caso especial para el 0
if numero_absoluto == 0:
    cantidad_digitos = 1
else:
    while numero_absoluto > 0:
        numero_absoluto //= 10  # Eliminamos el último dígito
        cantidad_digitos += 1

print("El número tiene", cantidad_digitos, "dígito/s.")


#ejercicio-3

numeroUno = int(input("Ingrese un número entero "))
numeroDos = int(input("Ingrese otro número entero "))
suma = 0
menor = min(numeroUno, numeroDos)
mayor = max(numeroUno, numeroDos)


for i in range(menor + 1, mayor):
    suma += i

print("La suma de los números ingresados es ", suma)

#ejercicio-4

num = int(input("Ingrese un número para sumar o presione 0 para salir "))
suma = 0

while num != 0:
    suma += num
    num = int(input("Ingrese un número para sumar o presione 0 para salir "))

print("La suma de los números ingresados fue de ", suma)

#ejercicio-5
import random
numAleatorio = int(input("Adivine el número secreto. Pista su valor es entero y oscila entre 1 y 9 "))
numSecreto = random.randrange(0,11)
intento = 1

while numAleatorio != numSecreto and numAleatorio != 0:
    numAleatorio = int(input("Ingrese nuevamente un número o presione 0 para salir "))
    intento += 1

print("Tuviste ", intento, " intentos. El número secreto era ", numSecreto)

#ejercicio-6

for numero in range(100, -1, -1):
    if numero % 2 == 0 :
        print(f"Número: {numero}")

#ejercicio-7
numEntero = int(input("Ingrese un número entero positivo "))
suma = 0

if numEntero < 0:
    print("El número debe ser positivo")
else:
    for i in range(1, numEntero + 1):
        suma += i
        print(f"La suma del número ingresado es igual a {suma}")

#ejercicio-8
contadorPares = 0
contadorImpares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input("Ingrese un número: "))

    if num % 2 == 0:
        contadorPares += 1
    else:
        contadorImpares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print(f"De los números ingresados se contabilizaron {contadorPares} N. Pares, {contadorImpares} N. Impares, {positivos} N. Positivos y {negativos} N. Negativos")

#ejercicio-9

ingresos = 100
suma = 0

for i in range(ingresos):
    nume = int(input("Escriba un número entero "))
    suma += nume

media = suma / ingresos
print(f"El valor promedio de los números ingresados es de {media}")

#ejercicio-10

numeInvertido = str(input("Dime un número de al menos dos cifras "))
invertido = numeInvertido[::-1]
invertido = int(invertido)
print(f"El número invertido es: {invertido}")
