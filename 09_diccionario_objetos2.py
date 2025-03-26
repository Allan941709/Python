#iniciar un objeto vacio
jugador = {}
print(jugador)

#agregar propiedades al objeto
jugador["nombre"] = "Allan" #al asignar un valor a una clave se usa el = 
jugador ["puntaje"] = 0
print(jugador)

#incrementar el puntaje
jugador["puntaje"] += 100
print(jugador)
jugador["puntaje"] += 200
print(jugador)

#acceder a un valor
print (jugador.get('consola', 'No existe esa propiedad')) #si no existe la propiedad se puede agregar un mensaje

#iterar sobre un objeto
for llave, valor in jugador.items(): #items() devuelve una lista de tuplas
    print(f'{llave} = {valor}')

#eliminar
del jugador['puntaje']
print(jugador)




