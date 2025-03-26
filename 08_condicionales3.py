#operadores and y or
#and: si las dos condiciones son verdaderas
#or: si una de las dos condiciones es verdadera
#nos siven para revisar 2 condicionales o mas al mismo tiempo
#and
usuario = True
usuario_admin = False
if usuario and usuario_admin:
    print("administrador")
elif usuario:
    print("acceso al sistema")
else: 
    print('debes iniciar sesion')

#or
usuario = False
usuario_admin = False
if usuario or usuario_admin: #evalua si el usuario es autenticado o admin 
    print("administrador")
elif usuario:
    print("acceso al sistema")
else:
    print('debes iniciar sesion')
