#Estructura de Datos Complejos

#Ejercicio01
# Agregar furtas y respectivos precios al siguiente diraccionario

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio02
# Actulizar precios de las siguientes frutas

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)


#Ejercicio03
# Crear una lista con el diccionario anterior, que solo contenga las frutas

frutas = list(precios_frutas.keys())

print(frutas)


#Ejercicio04
# Crear un programa que permita almacenar y consultar números telefónicos

contactos = {}

# Llenamos el diccionario con contactos

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {1+i}: ").strip()
    numero = input(f"Ingresá su número de teléfono de {nombre}: ").strip()
    contactos[nombre] = numero

# Se muestra el diccionario, a fin de verificar la información cargada

print("\nAgenda cargada:")
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")


# Consultar el contacto deseado

consulta = input("\nIngresá el nombre del contacto que querés buscar: ").strip()

# Verificar si existe y mostrar el número
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"No se encontró el contacto: {consulta}")


#Ejercicio05
# Crear un programa que solicite una frase y la imprima
# Pedimos la frase

frase = input("Ingresá una frase: ").strip()

# Separamos en palabras (por defecto split() divide por espacios)
palabras = frase.split()

# Creamos el set de palabras únicas
palabras_unicas = set(palabras)

# Mostramos el set
print("\nPalabras únicas:")
print(palabras_unicas)

# Creamos el diccionario de conteo
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Mostramos el diccionario
print("\nConteo de palabras:")
for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra}: {cantidad}")



#Ejercicio06
# Tuplas

# Creamos el diccionario vacío
alumnos = {}

# Pedimos los datos de 3 alumnos

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ").strip()
    
    # Pedimos 3 notas y las convertimos en enteros con float

    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    
    # Guardamos la tupla de notas
    alumnos[nombre] = tuple(notas)

# Calculamos y mostramos los promedios con dos decimales

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


#Ejercicio07
# Sets de dos números

parcial1 = {100, 75, 86, 45}
parcial2 = {91, 100, 29, 55}

# Los que aprobaron ambos parciales → intersección
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Los que aprobaron solo uno de los dos → diferencia simétrica
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# Los que aprobaron al menos uno → unión
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)



#Ejercicio08
# Crear un diccionario con claves (productos) y valores (stock)

# Diccionario inicial de productos con stock
stock_productos = {
    'Pan': 10,
    'Jabon': 5,
    'Arroz': 12
}

# Mostramos el stock inicial 
print("Stock inicial:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock}")

# Consultamos un producto
producto_consulta = input("\nIngresá el nombre del producto a consultar o actualizar: ").strip()

# Verificamos si el producto existe (ignorando mayúsculas/minúsculas)
encontrado = None
for prod in stock_productos:
    if prod.lower() == producto_consulta.lower():
        encontrado = prod
        break

if encontrado:
    print(f"El stock actual de {encontrado} es: {stock_productos[encontrado]}")
    try:
        agregar = int(input(f"¿Cuántas unidades querés sumar al stock de {encontrado}? "))
        stock_productos[encontrado] += agregar
        print(f"Nuevo stock de {encontrado}: {stock_productos[encontrado]}")
    except ValueError:
        print("Por favor ingresá un número válido.")
else:
    try:
        nuevo_stock = int(input(f"{producto_consulta} no existe. Ingresá el stock inicial para agregarlo: "))
        stock_productos[producto_consulta] = nuevo_stock
        print(f"Producto {producto_consulta} agregado con stock {nuevo_stock}.")
    except ValueError:
        print("Por favor ingresá un número válido.")

# Finalmente mostramos el stock final
print("\nStock actualizado:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock}")



#Ejercicio09
# Crar una agenda con claves (tuplas) y valores (eventos)

# Creamos la agenda con claves tupla (día, hora)
agenda = {
    ('Lunes', '10:00'): 'Reunión equipo',
    ('Martes', '08:00'): 'Clase de Python',
    ('Miércoles', '09:00'): 'Fisioterapia con Marga',
    ('Jueves', '16:00'): 'Entrega proyecto',
    ('Viernes', '12:00'): 'Almuerzo en Flia'
}

# Pedimos al usuario día y hora para consultar. Utilizando .capitalize podemos normalizar el formato del día
dia = input("Ingresá el día (ej: Lunes): ").strip().capitalize()
hora = input("Ingresá la hora (ej: 10:00): ").strip()

# Buscamos el evento en la agenda
clave = (dia, hora)
if clave in agenda:
    print(f"Evento para {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"No hay eventos programados para {dia} a las {hora}.")



#Ejercicio10

# Diccionario original: países y capitales
pais_capital = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago de Chile",
    "Uruguay": "Montevideo"
}

# Diccionario invertido: capitales como claves, países como valores
capital_pais = {}

for pais, capital in pais_capital.items():
    capital_pais[capital] = pais

# Mostrar el resultado
print("Diccionario invertido (capital: país):")
print(capital_pais)


