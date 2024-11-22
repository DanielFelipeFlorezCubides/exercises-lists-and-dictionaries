# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas 
# de la lista y <nota> cada una de las correspondientes notas introducidas 
# por el usuario.
import json
def read_file(path):
        with open(f'dataBases/ThirdExercises/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'dataBases/ThirdExercises/{path}', 'wb+') as file:
        convertJson = json.dumps(data, indent=4).encode('utf-8')
        file.write(convertJson)
        file.close()
        
def subjects_List():
    subjectData = read_file('thirdExercisesList.json')
    subject = input('Please type the subject you wanna storage: ')
    grade = int(input(f'Please type the grade you scored on {subject}: '))
    subjectData.append([subject, grade])
    subjectData.sort()
    write_file(subjectData, 'thirdExercisesList.json')
    return subjectData

def imprimir(subjects):
     if subjects:
          data = read_file('thirdExercisesList.json')
          subjectsList = len(data)
          print('Subjects list')
          for i in range(0, subjectsList):
               print(f'En {data[i][0]} has sacado {data[i][1]}')

# Escribir un programa que guarde en un diccionario los precios de 
# las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número 
# de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello.

def searchFruit(fruit):
    data = read_file('thirdExercisesDic.json')
    if data.get(fruit):
        return data.get(fruit)
    else:
         return ('Fruit not found')
    
