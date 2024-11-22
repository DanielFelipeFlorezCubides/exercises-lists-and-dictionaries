# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas 
# de la lista y <nota> cada una de las correspondientes notas introducidas 
# por el usuario.
from logic.thirdExercises import subjects_List, imprimir, searchFruit
def design():
    result = subjects_List()
    imprimir(result)
    return 0

# Escribir un programa que guarde en un diccionario los precios de 
# las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número 
# de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello.

def secondDesign():
    fruit = input("Please type fruit's name to search it's each pound value (Platano / Manzana / Pera / Naranja): ")
    info = searchFruit(fruit)
    print(f'This is the requested info {info}')
    kilos = float(input('Now please type you selected fruit purchase weight in kg please: '))
    if fruit == 'Platano':
        resultP = 1.35 * kilos
        print(f'The total ammount is: {round(resultP)} dollars')
    elif fruit == 'Manzana':
        resultM = 0.80 * kilos
        print(f'The total ammount is: {round(resultM)} dollars')
    elif fruit == 'Pera':
        resultPe = 0.85 * kilos
        print(f'The total ammount is: {round(resultPe)} dollars')
    elif fruit == 'Naranja':
        resultN = 0.70 * kilos
        print(f'The total ammount is: {round(resultN)} dollars')
    return 0