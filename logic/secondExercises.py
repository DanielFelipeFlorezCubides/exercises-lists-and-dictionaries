# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.
import json
def read_file(path):
        with open(f'dataBases/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'dataBases/{path}', 'wb+') as file:
        convertJson = json.dumps(data, indent=4).encode('utf-8')
        file.write(convertJson)
        file.close()

def subjects_List(subject):
    data = read_file('secondExercisesList.json')
    data.append(subject)
    data.sort()
    write_file(data, 'secondExercisesList.json')
    return data

def splitting():
    data = read_file('secondExercisesList.json')
    materias = len(data)
    for i in range(0, materias):
        print(f'''I'm studying: {data[i]}''')