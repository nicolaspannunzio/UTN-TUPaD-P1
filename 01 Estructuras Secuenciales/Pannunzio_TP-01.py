import math
from re import match

#ejercicio 1
print("hola mundo")

#ejercicio2
name = input("Escribe tu nombre: ")
print(f"Hola {name}")

#ejercicio3
name = input("Escribe tu nombre ")
lastname = input ("Escribe tu apellido ")
age = input ("Escribe tu edad ")
location = input ("En que ciudad vives ")
print(f"Soy {name} {lastname},  y tengo {age}  años y vivo en {location}")

#ejercicio4
import math
radio = float (input ("Asigne un valor numérico para el radio:" ))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El valor del area es  {area}")
print(f"El valor del perímetro es {perimetro}")

#ejercicio5
segundos = int (input ("Dime un número que lo convertire de segundos a horas "))
horas = segundos / 3600
print(f"Esos {segundos} segundos, equivalen a {horas} horas")

#ejercicio6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for ej6i in range(1, 11):
    ej6resultado = numero * ej6i
    print(f"{numero} x {ej6i} = {ej6resultado}")

#ejercicio7
numero1 = int(input("Ingrese un número entero, distinto de cero "))
numero2 = int(input("Ingrese otro número entero, distinto de cero "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print(f"La suma de {numero1} y {numero2} es {suma}")
print(f"La resta de {numero1} y {numero2} es {resta}")
print(f"La division de {numero1} y {numero2} es {division}")
print(f"La multiplicacion de {numero1} y {numero2} es {multiplicacion}")

#ejercicio8
altura = float(input("Ingrese su altura "))
peso = float(input("Ingrese su peso "))
imc = peso / (altura **2)
print(f"Su indice de masa corporal es {imc}")

#ejercicio9
celsius = float(input("Ingrese una temperatura en grados celsius "))
fahre = ((9 / 5) * celsius) + 32
print(f"El equivalente en grados Fahrenheit es {fahre}")

#ejercicio10
num1 = float(input("Ingrese un número "))
num2 = float(input("Ingrese nuevamente un número "))
num3 = float(input("Ingrese un último número "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los numeros ingresados es {promedio}")