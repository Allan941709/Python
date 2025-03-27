#metodos 
texto = "Hola, mundo!"

# Método upper() - Convierte el texto a mayúsculas
print(texto.upper())

# Método lower() - Convierte el texto a minúsculas
print(texto.lower())

# Método capitalize() - Capitaliza la primera letra mayuscula
print(texto.capitalize())

# Método replace() - Reemplaza una subcadena por otra
print(texto.replace("mundo", "Python"))

# Método split() - Divide el texto en una lista
print(texto.split(", "))

# Método strip() - Elimina espacios en blanco al inicio y al final
texto_con_espacios = "   Hola, mundo!   "
print(texto_con_espacios.strip())

#Otros metodos
# Método find() - Encuentra la posición de una subcadena
print(texto.find("mundo"))

# Método count() - Cuenta cuántas veces aparece una subcadena
print(texto.count("o"))

# Método startswith() - Verifica si el texto comienza con una subcadena
print(texto.startswith("Hola"))

# Método endswith() - Verifica si el texto termina con una subcadena
print(texto.endswith("!"))

# Método isalpha() - Verifica si todos los caracteres son alfabéticos
print(texto.isalpha())  # Nota: Esto será False debido a la coma y el espacio

# Método isdigit() - Verifica si todos los caracteres son dígitos
print("12345".isdigit())