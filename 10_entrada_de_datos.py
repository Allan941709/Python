
#entrada de datos input()
nombre = input('Cual es tu Nombre?: \r\n')  # \r\n es un salto de linea
print(f'Hola {nombre}') #f para anexar un texto

#como leer datos numericos
#edad = input('Cual es tu Edad?: \r\n')
#if edad >= 18:
    #print('Eres mayor de edad')
#else:
    #print('Eres menor de edad')
#TypeError: '>=' not supported between instances of 'str' and 'int'
#para solucionar el error se debe convertir el dato a entero

edad = int(input('Cual es tu Edad?: \r\n')) #tambien se puede convertir a float, str, etc
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')


#ejercicio juego 
numero = int(input('Agreganun numero y te dire si es par o impar: \r\n'))
if numero % 2 == 0: #el modulo % devuelve el residuo de una division
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

#reto#####################################################################################
nombre__alumno = input('Cual es tu Nombre?: \r\n')
print(f'Hola {nombre__alumno} Ahora responde las siguientes preguntas con un si o no')

#preguntas
pregunta1 = input('Te gusta la pizza? \r\n')
pregunta2 = input('Te gusta el futbol? \r\n')
pregunta3 = input('Te gusta el cine? \r\n')
print(f'{nombre__alumno} tus respuestas fueron: \r\n')

#respuestas
print(f'1. Te gusta la pizza? {pregunta1}')
print(f'2. Te gusta el futbol? {pregunta2}')
print(f'3. Te gusta el cine? {pregunta3}')

#calificacion 
calificacion = 0
if pregunta1 == 'si':
    calificacion += 1
if pregunta2 == 'si':
    calificacion += 1
if pregunta3 == 'si':
    calificacion += 1
print(f'Tu calificacion es de {calificacion} de 3')
