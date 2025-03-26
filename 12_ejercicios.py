#aplicando todo hasta ahora
#app nombrar una playlist y agregar canciones
#creamos la variable que se usa en varaibles globales para usar en todas las funciones
playlist = {} #diccionario vacio (Objeto)
playlist['canciones'] = [] #lista vaccia (Array)
#funcion principal
def app():
   
   #agregar playlist
   agregar_playlist = True
   while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar la playlist: \r\n')
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            
            #ya no se agrega mas playlist
            agregar_playlist = False

            #llamamos a la funcion para agregar canciones
            agregar_canciones() #llamamos a la funcion

#funcion para agregar canciones
def agregar_canciones():
    #agregar canciones
    agregar_cancion = True

    while agregar_cancion:
        #preguntar al usuario que cancion desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'Agrega una cancion para la playlist {nombre_playlist}: \r\n'
        pregunta += 'escribe "X" para dejar de agregar canciones \r\n'


        cancion = input(pregunta)

        if cancion == 'X':
            #dejar de agregar canciones
            agregar_cancion = False

            #mmostrar resumen de la playlist
            mostrar_resumen()


        else: 
            #agregar la cancion a la playlist
            playlist['canciones'].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']



    print(f'Plalist: {nombre_playlist}\r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
    



app()
