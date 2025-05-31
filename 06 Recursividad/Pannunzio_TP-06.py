#ejercicio 1
#Factorial de un número se calcula con la fórmula n! = n x (n-1) x (n-2)...

def factorial(n):
    #caso base
    if n == 0:
        return 1
    
    #caso recursivo
    return n * factorial(n-1)

num = int(input("Ingrese un número entero positivo: "))

if num < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    print(f"Los factoriales del 1 al {num}:")

    for i in range (1, num +1):
        print(f"{i}! = {factorial(i)}")



#ejercicio 2
#Serie de Fibonacci

#Posición:     0   1   2   3   4   5   6   7   8
#Valor:        0   1   1   2   3   5   8  13  21
#fib(n) = fib(n - 1) + fib(n - 2) --> fórmula general para calcular la serie

# Casos bases
# fib(0) = 0
# fib(1) = 1

# Pensamiento recursivo
# Si n == 0 → retorno 0
# Si n == 1 → retorno 1
# Si n > 1 → retorno fib(n - 1) + fib(n - 2)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Paso 1: Pedimos al usuario un número
posicion = int(input("Ingresá hasta qué posición querés ver la serie de Fibonacci: "))

# Paso 2: Validamos que sea no negativo
if posicion < 0:
    print("La posición debe ser 0 o mayor.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")


#ejercicio 3
# crear una función recursiva que calcule la potencia de un número base elevado a un exponente
# n^m = n * n * n * ... * n   (m veces) --> elevando la base n a un exponente m 

# caso base
# Si m == 0 → n^0 = 1


def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

# Pedimos los datos al usuario
base = int(input("Ingresá la base (número entero): "))
exponente = int(input("Ingresá el exponente (entero ≥ 0): "))

# Validamos el exponente
if exponente < 0:
    print("El exponente debe ser mayor o igual a 0.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")


#ejercicio 4
# Conversión de un número decimal a binario

# caso base: cuando el número es 1 o 0
# entonces --> Si n < 2: retornar str(n)

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Algoritmo general
print("Conversor Decimal a Binario (recursivo)")
numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"{numero} en binario es: {binario}")


#ejercicio 5
# Un políndromo es una palabra que se lee igual de izq a derecha y viceversa. Ej neuquen

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Algoritmo principal
print("Verificador de Palíndromos (recursivo)")
texto = input("Ingresá una palabra (sin espacios ni tildes): ").lower()

if texto.isalpha():
    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo ')
    else:
        print(f'"{texto}" no es un palíndromo ')
else:
    print("Ingresá solo letras sin espacios ni caracteres especiales.")


#ejercicio 6
# sumar los dígitos de un número usando recursividad

#caso base --> cuando el número llega a 0, retornanos 0

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

# Algoritmo principal
print("Sumador de Dígitos (recursivo)")
numero = int(input("Ingresá un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")


#ejercicio 7

#caso base --> n == 1 porque solo necesitamos un bloque, entonces devolvemos 1
#pensamiento recursivo --> contar_bloques(n) = n + contar_bloques(n - 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Algoritmo principal
print("Calculadora de bloques para pirámide (recursiva)")
nivel_mas_bajo = int(input("¿Cuántos bloques hay en el nivel más bajo? "))

if nivel_mas_bajo < 1:
    print("Debe ingresar un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_mas_bajo)
    print(f"Se necesitan {total} bloques en total para construir la pirámide.")


#ejercicio 8
#contador de dígitos

#pensamiento recursivo --> el ultimo dígito num % 10 y el resto del num es num // 10
#caso base --> cuando el número es 0, no quedan más digitos por comprobar, entonces devolvemos 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)

# Algoritmo principal
print("Contador de Dígitos (recursivo)")
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("¿Qué dígito (0-9) querés contar? "))

if numero < 0 or digito < 0 or digito > 9:
    print("Número positivo y dígito entre 0 y 9, por favor.")
else:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en {numero}.")
