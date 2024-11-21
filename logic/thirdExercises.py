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
        
def subjects_List(subject):
    subjectData = read_file('thirdExercisesList.json')
    subjectData.append(subject)
    subjectData.sort()
    write_file(subjectData, 'thirdExercisesList.json')
    return subjectData

def splitting(grade):
    data = read_file('thirdExercisesList.json')
    materias = len(data)
    for i in range(0, materias):
        print(f'''En {data[i]} has sacado: {grade[i]}''')