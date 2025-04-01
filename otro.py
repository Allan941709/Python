#count()
#En Listas
numeros = [1,2,3,2,4,2,5]
cantidad_dos = numeros.count(2)
print("El numero 2 aparece:", cantidad_dos, "veces") #salida: 3

#En Cadenas
cadena = "Python es un lenguaje de Programacion Python"
cantidad_mundo = cadena.count("mundo")
print("La palabra 'mundo' aparece:", cantidad_mundo, "veces") # salida: 2

#len()
lista = [10, 20, 30, 40]
print("Longitud de la lista:", len(lista)) #Salida: 4

cadena = "Hola Mundo"
print("Numero de caracteres:", len(cadena)) #Salida: 10


#find()
mensaje = "Bienvenido a Python"
pos = mensaje.find("Python")
print("La palabra 'Python' Comienza en el indice:", pos) #Salida: 14
#No Encontrado 
pos_no = mensaje.find("Java")
print("La palabra 'Java' se encontro en:", pos_no) #Salida: -1

#split()
oracion = "Aprender Python es divertido"
palabras = oracion.split()
print(palabras) #Salida: ['Aprender', 'Python', 'es', 'divertido']
#Dividiendo por separador especifico
datos = "manzana,banana,pera"
frutas = datos.split(",")
print(frutas) #Salida: ['manzana', 'banana', 'pera']

#join()
palabras = ['Pyton', 'es', 'potente']
frase = " ".join(palabras)
print(frase) #Salida: "Python es potente"
#usando separador
csv = ",".join(palabras)
print(csv) #Salida: "Python, es, potente"

#replase()
mensaje = "Programando con Java"
nuevo_mensaje = mensaje.replace("Java", "Python")
print(nuevo_mensaje) #Salida: "Programando con Python"

#slicing()
#Con listas
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublista = numeros[2:7] #Desde el idice 2 hasta el 6 
print(sublista)  #[2, 3, 4, 5, 6]
sublista2 = numeros[2:7:2]  #Desde el indice 2 hasta el 6, de 2 en 2
print(sublista2) #Salida: [2, 4, 6]
#con cadenas
texto = "ABCDEFGHIJKLM"
subcadena = texto[3:10] #Caracteres desde el indice 3 hasta el 9
print(subcadena) #Salida: "SEFGHIJ"

#strip()
texto = " Hola, Python "
limpio = texto.strip()
print(f"'{limpio}'") #Salida: 'Hola Python'

texto2 = "###Hola, Python###"
limpio2 = texto2.strip("#")
print(f"'{limpio2}'") #Salida: "Hola, Python"

#upper() y lower()
texto = "Python Es Genial"
print(texto.upper()) #Salida: "PYTHON ES GENIAL"
print(texto.lower()) #Salida: "python es genia"