#revisar si una condicion es mayor a 
balance = 500 
if balance >0:
    print("puedes pagar")

#if else 
balance2 = 0 #mi saldo es 0
if balance2 > 0: #si mi saldo es mayor a 0
    print("puedes pagar")
else: 
    print("no puedes pagar") #si mi saldo es menor a 0 cumple esta funcion

#mayor o igual a
visitas = 5
if visitas >= 5: #si mis visitas son mayor o igual a 5
    print("excelente")
else:
    print("no es igual a 5")

#con diciones igual a
likes = 200
if likes == 200:
    print("excelente")
else:
    print("no es igual a 200")

#comparaciones con texto
lenguaje = "Python"
if lenguaje == "Python":
    print("Excelente desicion")

#diferecia de texto
lenguaje2 = "Python"
if lenguaje2 != "Java":
    print("Excelente desicion")

#evaluar booleanos
usuario_aut = True
if usuario_aut : #al evaluar valores booleanos no es necesario poner == True
    print("puedes continuar")
else:
    print("no puedes continuar")

#if anidados
#evaluar elementos de la lista
programas = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
if 'php' in programas:
    print("php si esta en la lista")
else:
    print("php no esta en la lista")

#if anidados
usuario_aut = True
usuario_admin = True
if usuario_aut : #al evaluar valores booleanos no es necesario poner == True
    if usuario_admin:
        print("acceso total") #evalua si el usuario es admin
    else:
        print("acceso al sistema") #evalua si el usuario es autenticado
else:
    print("no puedes continuar")
