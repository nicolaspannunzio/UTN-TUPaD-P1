def menu_principal():
    print("\n===== SIMULADOR DE SISTEMAS NUMÉRICOS Y LÓGICA BINARIA =====")
    print("1. Conversor de Sistemas Numéricos")
    print("2. Contador Binario")
    print("3. Calculadora Bit a Bit")
    print("4. Sumador de 1 Bit")
    print("5. Adivinanzas en binario")
    print("6. Salir")
    return input("Seleccioná una opción: ")

# Funciones a implementar
def conversor_numerico():
    print("\n=== Conversor de números decimales a: Binario / Octal / Hexadecimal ===")

    while True:
        entrada = input("Ingresá un número decimal (o escribí 'salir' para volver al menú): ")

        if entrada.lower() == 'salir':
            break

        if entrada.isdigit():
            numero = int(entrada)
            binario = bin(numero)[2:]
            octal = oct(numero)[2:]
            hexadecimal = hex(numero)[2:].upper()

            print(f"\nBinario: {binario}")
            print(f"Octal: {octal}")
            print(f"Hexadecimal: {hexadecimal}\n")
        else:
            print("⚠️ Entrada no válida. Por favor, ingresá un número decimal positivo.")


def contador_binario():
    print("\n[ Módulo en desarrollo: Contador Binario ]")
    # Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
    # Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.

    import time  # Importa la librería para poder hacer pausas

    # Recorre los números del 0 al 15
    for i in range(16):
        num = i         # Guarda el número actual en una variable auxiliar
        binario = 0     # Variable que almacenará el número en binario (como número decimal)
        lugar = 1       # Representa la posición del bit (1, 10, 100, 1000...)

        # Bucle para calcular los 4 bits (de derecha a izquierda)
        for j in range(4):
            binario += (num % 2) * lugar  # Extrae el bit menos significativo y lo suma en la posición correcta
            num = num // 2                # Divide el número entre 2 para avanzar al siguiente bit
            lugar *= 10                   # Pasa a la siguiente posición decimal (unidad → decena → centena...)

        # Imprime el número original y su representación binaria (en forma numérica)
        print(f"{i} -> {binario}")
        time.sleep(0.5)  # Espera de medio segundo antes de pasar al siguiente número

def calculadora_bit_a_bit():
    # Calcula y muestra operaciones bit a bit (AND, OR, XOR) entre dos números.
    # Muestra los resultados en formato decimal y binario.
    print("\n--- Calculadora de Operaciones Bit a Bit (AND, OR, XOR) ---")

    # Función auxiliar para obtener un número entero válido
    def obtener_entero(mensaje):
        while True:
            entrada_str = input(mensaje)

            # Validación de la entrada
            es_negativo = False
            if entrada_str.startswith('-'):
                es_negativo = True
                temp_str = entrada_str[1:]
            else:
                temp_str = entrada_str

            # Comprobar si son dígitos y no está vacío
            if temp_str.isdigit() and temp_str != '':
                # Convertir a entero
                if es_negativo:
                    numero = int("-" + temp_str)
                else:
                    numero = int(temp_str)

                return numero # Retorna el número válido
            else:
                print("Entrada no válida. Por favor, ingresa un número entero.")

    # Obtener los dos números usando la función auxiliar
    num1 = obtener_entero("Ingresá el primer número entero: ")
    num2 = obtener_entero("Ingresá el segundo número entero: ")

    # Mostrar la representación binaria de los números de entrada
    print(f"\nRepresentación binaria de {num1}: {bin(num1)}")
    print(f"Representación binaria de {num2}: {bin(num2)}")

    # Realizar y mostrar operación AND
    resultado_and = num1 & num2
    print("\n--- Resultado AND ---")
    print(f"Decimal: {num1} & {num2} = {resultado_and}")
    print(f"Binario: {bin(num1)} & {bin(num2)} = {bin(resultado_and)}")

    # Realizar y mostrar operación OR
    resultado_or = num1 | num2
    print("\n--- Resultado OR ---")
    print(f"Decimal: {num1} | {num2} = {resultado_or}")
    print(f"Binario: {bin(num1)} | {bin(num2)} = {bin(resultado_or)}")

    # Realizar y mostrar operación XOR
    resultado_xor = num1 ^ num2
    print("\n--- Resultado XOR ---")
    print(f"Decimal: {num1} ^ {num2} = {resultado_xor}")
    print(f"Binario: {bin(num1)} ^ {bin(num2)} = {bin(resultado_xor)}")


def sumador_un_bit():
    # SUMADOR DE 1 BIT
    # a b = A S     a b  AND      # a b  XOR
    # 0 0   0 0     0 0   0       # 0 0   0
    # 0 1   0 1     0 1   0       # 0 1   1
    # 1 0   0 1     1 0   0       # 1 0   1
    # 1 1   1 0     1 1   1       # 1 1   0

    # Esta función recibe los dos dígitos binarios a sumar.
    # Retorna una tupla con los bits de carry y de suma.
    def suma(a, b):
        suma= a ^ b # El bit de suma equivale a la tabla de XOR
        carry= a & b # El bit de acarreo equivale a la tabla de verdad de un AND
        return carry, suma

    # Esta función valida que el dato ingresado sea un 0 o un 1
    # y lo retorna.
    def validador_bin():
        while True:
            n=input("")
            if n!="1" and n!="0":
                print("Ingrese un valor valido (1 o 0): ", end="")
            else:
                n=int(n)
                return n

    print("##### SUMADOR DE 1 BIT #####")

    while True:
        print("\nIngrese el primer bit:  ", end="")
        a = validador_bin()

        print("Ingrese el segundo bit: ", end="")
        b = validador_bin()

        # Enviamos a la función 'suma' los valores a y b, a la vez que guardamos la tupla en la variable 'resultados'
        resultados= suma(a,b)

        print("\nBit de acarreo:",resultados[0])
        print("Bit de suma:", resultados[1])

        while True:
            fin = input('\n¿Quiere seguir sumando o volver al menú principal? (y/n): ')
            if fin.lower() == 'n':
                print('Gracias por sumar. Volviendo al menú principal...')
                return
            elif fin.lower() == 'y':
                break
            else:
                print("Opción no válida. Ingrese 'y' para continuar o 'n' para volver al menú principal.")

#Se im porta la libreria random para generar numeros aleatorios
import random

def adivinanzas_en_binario():
    def decimalABinario(n):
        return bin(n)[2:]

    def binarioADecimal(n):
        return int(n, 2)

    #Se inicia el juego
    while True:
        modo = random.choice(['decimal', 'binario']) # Se elige aleatoriamente entre decimal y binario
        if modo == 'binario': # Si el modo es binario, se convierte un número decimal a binario
            num = random.randint(0,100)
            binario = decimalABinario(num)
            print(f'\n¿Qué número es {binario} en decimal?')
            respuesta = input('Tu respuesta: ')
            if respuesta == str(num): # Se compara la respuesta del usuario con el número decimal
                print('¡Correcto!')
            else:
                print(f'Incorrecto. El número es {num}')
        else: # Si el modo es decimal, se convierte un número binario a decimal
            num = random.randint(0, 100)
            print(f'\n¿Qué número es {num} en binario?')
            respuesta = input('Tu respuesta: ')
            if respuesta == decimalABinario(num):
                print('¡Correcto!')
            else:
                print(f'Incorrecto. El número es {decimalABinario(num)}')

        fin = input('\n¿Quiere seguir jugando o volver al menú principal? (y/n): ')
        if fin.lower() == 'n':
            print('Gracias por jugar. Volviendo al menú principal...')
            return #Se vuelve al menú principal unicamente si el usuario escribe 'n'

# Loop principal del programa
while True:
    opcion = menu_principal()

    if opcion == "1":
        conversor_numerico()
    elif opcion == "2":
        contador_binario()
    elif opcion == "3":
        calculadora_bit_a_bit()
    elif opcion == "4":
        sumador_un_bit()
    elif opcion == "5":
        adivinanzas_en_binario()
    elif opcion == "6":
        print("¡Hasta la próxima!")
        break
    else:
        print("⚠️ Opción no válida. Por favor, intentá de nuevo.")



################################################################
######### TP_Integrador -- Matemática & Programación I #########
######### Integrantes: #########################################
######### Medina - Olima - Pannunzio - Pavon - Perez ###########
################################################################