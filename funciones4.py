#metodos y Funciones diferencia
nombre = 'allan' #definimos una variable

#funcion su sintaxis 
def mostrar_nombre(nombre):
    print(f'Hola {nombre}')

mostrar_nombre(nombre) #llamamos a la funcion

#metodo su sintaxis
print(nombre.upper()) #llamamos al metodo upper
print(nombre.title()) #llamamos al metodo title 

#retos
#crear una funcion que imprima un mensaje de bienvenida
def bienvenida():
    print('Mi primera Bienvenida')
bienvenida()
  
#crear que tome un nombre de usuario y lo muestre como mensaje de bienvenida
def saludo(nombre):
    print(f'Hola {nombre}')
saludo('Allan')

#crear una funcion que tome la ultima actividad que hiciste 
def ultima_actividad(actividad):
    print(f'La ultima actividad que hiciste fue {actividad}')
ultima_actividad('Estudiar') 

#juntas
def actividad(nombre,saludar,actividades):
    print(f'Bienvendo {nombre} {saludar} {actividades}')

actividad('Allan','hola','estudiar')


