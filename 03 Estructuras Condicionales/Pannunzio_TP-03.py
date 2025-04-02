#ejercicio1
edad = int(input("Ingrese su edad "))
if edad >= 18:
    print("Ud es mayor de edad")
else:
    print("Ud es menor de edad")

#ejercicio2
nota = int(input("Ingrese su calificación de programación "))
if nota >= 6:
    print("Aprobado!")
else:
    print("Desaprobado!")

#ejercicio3
numeroPar = int(input("Ingrese un número par "))
if (numeroPar % 2 == 0):
    print("El número ingresado es par")
else:
    print("El número ingresado no es un número par")

#ejercicio4
edad = int(input("Ingrese su edad "))
if edad < 12:
    print("Eres apenas un niñx")
elif edad >= 12 and edad < 18 :
    print("Eres adolescente")
elif edad >= 18 and edad < 30 :
    print("Eres adulto joven")
elif edad >= 30 :
    print("Eres un adulto")

#ejercicio5
contrasenia = len(input("Ingrese su contraseña. La misma debe tener entre 8 y 14 caracteres "))
if  8 <= contrasenia <= 14:
    print("Contraseña válida")
else:
    print("Contraseña inválida")

#ejercicio6
from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")

#ejercicio7
frase = input("Dime una palabra que termine en una letra vocal ")
ultima_letra = frase[-1].lower()  
print(f"La ultima letra de la palabra es: {ultima_letra}") 

vocales = ["a","e","i","o","u"]
if ultima_letra in vocales:
    print(f"{frase}!")
else:
    print(f"Tu palabra {frase} no termina en vocal")

#ejercicio8
nombre = input("Ingrese su nombre de pila ")
opcion = input("Si deseas ver tu numbre en mayúsculas, presioná 1 o Si deseas ver tu numbre en mayúsculas, presioná 2  o Si deseas ver tu numbre en mayúsculas, presioná 3 ").strip()
#strip() para eliminar espacios antes o después de la opción ingresada

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción incorrecta")

#ejercicio9
terremoto = int(input("Ingrese la magnitud del terremoto según la escala de Ritcher. Los valores iran desde 1 hasta 7 "))
if terremoto < 3:
    print("Muy leve. (imperceptible)")
elif 3 <= terremoto < 4:
    print("Leve. (ligeramente preceptible)")
elif 4 <= terremoto < 5:
    print("Moderado")
elif 5 <= terremoto < 6:
    print("Fuerte")
elif 6 <= terremoto < 7:
    print("Muy fuerte")
elif 7 <= terremoto:
    print("Extremo")
else:
    print("El número ingresado es incorrecto")

#ejercicio10
hemisferio = input("Dime en qué hemisferio te encuentras (N/S): ").upper()
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
    "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
    "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}
mes = input("Dime el mes en el que estás: ").lower()
mes_numero = meses[mes]  
dia = int(input("Dime el día (1-31): "))

# Invierno (Hemisferio N) o Verano (Hemisferio S)
if (mes_numero == 12 and dia >= 21) or (mes_numero == 1) or (mes_numero == 2) or (mes_numero == 3 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Invierno en el Hemisferio Norte")
    else:
        print("Estás en Verano en el Hemisferio Sur")

# Primavera (Hemisferio N) o Otoño (Hemisferio S)
elif (mes_numero == 3 and dia >= 21) or (mes_numero == 4) or (mes_numero == 5) or (mes_numero == 6 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Primavera en el Hemisferio Norte")
    else:
        print("Estás en Otoño en el Hemisferio Sur")

# Verano (Hemisferio N) o Invierno (Hemisferio S)
elif (mes_numero == 6 and dia >= 21) or (mes_numero == 7) or (mes_numero == 8) or (mes_numero == 9 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Verano en el Hemisferio Norte")
    else:
        print("Estás en Invierno en el Hemisferio Sur")

# Otoño (Hemisferio N) o Primavera (Hemisferio S)
elif (mes_numero == 9 and dia >= 21) or (mes_numero == 10) or (mes_numero == 11) or (mes_numero == 12 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Otoño en el Hemisferio Norte")
    else:
        print("Estás en Primavera en el Hemisferio Sur")
