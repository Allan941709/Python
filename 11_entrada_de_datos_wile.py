#wile
#pregunta = 'Agrega un numero y te dire si es par o impar: \r\n'
#pregunta += '(Escribe "cerrar" para terminar el programa)'
#preguntar = True

#while preguntar:
#    numero = input(pregunta)
#    if numero == 'cerrar':
#        preguntar = False #para terminar el programa esta es la funcion principal de while al cumplise termina su trabajo  
#    else:
#        numero = int(numero)
#        if numero % 2 == 0:
#            print(f'El numero {numero} es par')
#        else:
#            print(f'El numero {numero} es impar')
#            
#while corre hasta que se cumpla la condicion
numero = 0 #se puede declarar la variable fuera del while
#while numero <= 10: #mientras numero sea menor o igual a 10
#    print(numero)
#    numero += 1 #aqui se incrementa por que si no se quedaria en 0 infinito

#if dentro de while
while numero <= 10:
    if numero == 5:
        print('Cinco!')
        break #termina el ciclo
    else:
        print(numero)
    numero += 1
    
        
