#ejercicio-01

lista = list(range(4,101,4))
print(lista)


#ejercicio-02

favoritos = ["Marga", "Tino", 7 , "pets", "home"]
print(favoritos[-2])


#ejercicio-03

nuevaLista = []
nuevaLista.append("carrot")
nuevaLista.append(True)
nuevaLista.append(7)
print("Lista resultante:", nuevaLista)

#otros métodos
# nueva_lista.extend(["carrot", True, 7])  
# nueva_lista += ["carrot", True, 7] 


#ejercicio-04

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("La nueva lista es ", animales)


#ejercicio-05
# en este ejercicio se presenta una lista de números y con la función remove y max, se busca el mayor y se elimina
nuemros = [8, 15, 3, 22, 7]
nuemros.remove(max(nuemros))
print(nuemros)


#ejercicio-06

nueva_lista = list(range(10,31,5))
print(nueva_lista[0], nueva_lista[1])

#alternativa --> print(nueva_lista[0], nueva_lista[1])


#ejercicio-07

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "kwin"
autos[2] = "sandero"
print("La lista actualizada de autos es:", autos)


#ejercicio-08

dobles = []
dobles.append(5 * 2)  
dobles.append(10 * 2) 
dobles.append(15 * 2) 
print(dobles)  

# alternativa --> dobles.extend([5 * 2, 10 * 2, 15 * 2]) 


#ejercicio-09

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")         
compras[1][1] = "tallarines"       
compras[0].remove("pan")           
print(compras)                     


#ejercicio-10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)