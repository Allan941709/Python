#creando un diccionario de objetos simples
canciones = {
    'artista': "Metallica", #clave: valor
    'cancion': "Enter Sandman",
    'lanzamiento': 1991,
    'album': "Metallica"

}
print(canciones)
print(canciones['artista']) #imprimiendo el valor de la clave 'artista'
print(canciones['lanzamiento']) 
#mesclar con un mensaje
print(f'estoy escuchando {canciones["cancion"]} de {canciones["artista"]}') #imprimiendo el valor de la clave 'cancion' y 'artista'

#agregando un nuevo valor al diccionario
canciones['genero'] = 'Rock'
print(canciones)

#modificando un valor del diccionario
canciones['cancion'] = 'Seek and Destroy'
print(canciones)

#eliminando un valor del diccionario
del canciones['lanzamiento']
print(canciones)