# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.
from logic.secondExercises import subjects_List, splitting, datos

def secondListDesign():
    subject = input('Please type the subject you wanna storage: ')
    subjects_List(subject)
    splitting()
    return 0

# Escribir un programa que pregunte al usuario su nombre, edad, dirección
# y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.
def secondDicDesign():
    name = input('Please type your name: ')
    age = int(input('Please type your age: '))
    address = input('Please type your address: ')
    phone = int(input('Please type your phone: '))
    datos(name, age, address, phone)
    print(f'{name} tiene {age} años, vive en {address} y su número de teléfono es {phone}.')