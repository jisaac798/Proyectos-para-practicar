import random
import string

print("Password: ")
"""importo las bibliotecas que (creo que) son propias de python, creo variables que almacenan los distintos caracteres de Ascii
   despues uso una funcion de la libreria random para agarrar caracteres aleatorios de las variables, y creando una cadena de caracteres
   de la longitud que quiera
"""
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
chars = lower + upper #+ numbers + symbols

temp = random.sample(chars, 8)
print("".join(temp))