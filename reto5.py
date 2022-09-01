"""
RETO 5:  
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se 
añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

dict1 = {}
n = int(input("Cuantos datos va a añadir? "))

for i in range(n):

    key = input("Digite el nombre del dato ")
    value = input("Digite el dato ")

    dict1[key] = value
    print(dict1)
