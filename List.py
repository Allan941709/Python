lenguajes = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
print(lenguajes[0]) #los arreglos empiezan en 0

#ordenar arreglo
lenguajes.sort()
print(lenguajes)

#acceder dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[4]}'
print(aprendiendo) 

#modificar un arreglo
lenguajes[0]= 'Ruby'
print(lenguajes)

#agregar un elemento
lenguajes.append('Go')
print(lenguajes)

#eliminar un elemento
del lenguajes[5] #este metodo elimina el elemento en la posicion 5
print(lenguajes)

#eliminar el ultimo elemento
lenguajes.pop() #este metodo elimina el ultimo elemento
print(lenguajes)

#eliminar con pop algun elemento en especifico
lenguajes.pop(1) #este metodo elimina el elemento en la posicion 1
print(lenguajes)

#eliminar por nombre
lenguajes.remove('C++')
print(lenguajes)

