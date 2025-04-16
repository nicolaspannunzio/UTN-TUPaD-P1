#ejercicio-1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#programa principal
imprimir_hola_mundo()


#ejercicio-2
nombre = input("¿Cómo te llamás? ")

#programa principal
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

print(saludar_usuario(nombre))


#ejercicio-3

# función para pedir nombre
def pedir_nombre():
    return input("Escribe tu nombre ")

# función para pedir apellido
def pedir_apellido():
    return input("Ahora, escribe tu apellido ")

# función para pedir edad
def pedir_edad():
    return input("Escribe tu edad ")

# función para pedir lugar de residencia
def pedir_residencia():
    return input("Escribe tu lugar de residencia ")


#programa principal
def informacion_personal (nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = pedir_nombre()
apellido = pedir_apellido()
edad = pedir_edad()
residencia = pedir_residencia()

print(informacion_personal(nombre, apellido, edad, residencia))


#ejercicio-4
import math
def area(radio):
    return math.pi * (radio ** 2)
def perimetro(radio):
    return 2 * math.pi * radio


#programa principal
radio = float(input("Por favor, escribí el radio del círculo: "))

def calcular_area_circulo(radio):
    return area(radio)

def calcular_perimetro_circulo(radio):
    return perimetro(radio)

print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")


#ejercicio-5
def segundos(segundos):
    return segundos/3600


#programa principal
segundos_ingresados = int(input("Por favor dígame los segundos que lleva esperando a que el programa funcione: "))
horas_resultado = segundos(segundos_ingresados)


print(f"Según mis cálculos, te ha llevado tiempo tu programa... ¡precisamente {horas_resultado:.2f} horas! Buen trabajo :)")


#ejercicio-6
#num = int(input("Escribe un número para mostrarte su tabla de multiplicar "))
def multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#programa principal
def tabla_multiplicar(numero):
    return multiplicar(numero)

# Validación de datos
while True:
    entrada = input("Escribí un número entero positivo: ")
    
    if not entrada.isdigit():       #función de las cadenas (strings)
        print("Error: Debés ingresar solo números positivos.")
        continue

    num = int(entrada)
    
    if num <= 0:
        print("Error: El número debe ser mayor que cero.")
        continue
    
    # Si todo está bien, salgo del bucle
    break

tabla_multiplicar(num)


#ejercicio-7
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir por cero"

a = int(input("Ingresá un número entero positivo "))
b = int(input("Ingresá otro número entero positivo "))

#programa principal
def operaciones_basicas(a, b):
    return (sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b))

suma, resta, multi, divi = operaciones_basicas(a, b)
print(f"La suma de los números ingresados es: {suma}")
print(f"La resta de los números ingresados es: {resta}")
print(f"La multiplicación de los números ingresados es: {multi}")
print(f"La división de los números ingresados es: {divi}")


#ejercicio-8

# Función principal
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en centímetros: ")) / 100  # Conversión a metros

imc = calcular_imc(peso, altura)
print(f"Índice de masa corporal es: {imc:.2f}")         # .2f últil para redondeo con dos decimales 


#ejercicio-9
def fah (celsius):
    return (celsius * 9/5) + 32

#programa principal
temperatura = int(input("Diga la temperatura de su ciudad en grados Celsius "))

def celsius_a_fahrenheit(celsius):
    return fah(celsius)

resultado = celsius_a_fahrenheit(temperatura)
print(f"La temperatura equivalente en grados Fahrenheit en tu ciudad es de {resultado:.2f} ")


#ejercicio-10

def promedio (a, b, c):
    return (a + b + c) / 3

a = int(input("Ingresá un primer valor "))
b = int(input("Ingresá un segundo valor "))
c = int(input("Ingresá un tercer valor "))

#programa principal
def calcular_promedio(a, b, c):
    return promedio (a, b, c)

resultado = calcular_promedio(a, b, c)
print(f"El promedio de los tres números ingresados es de {resultado:.2f}")