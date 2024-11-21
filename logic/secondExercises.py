# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.
import json
def read_file(path):
        with open(f'dataBases/SecondExercises/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'dataBases/SecondExercises/{path}', 'wb+') as file:
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
        
# Escribir un programa que pregunte al usuario su nombre, edad, dirección
# y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.

def datos(name, age, address, phone):
    data = read_file('secondExercisesDic.json')
    datosDic = [{
        'name': name,
        'age': age,
        'address': address,
        'phone': phone
    }]
    data.append(datosDic)
    write_file(data, 'secondExercisesDic.json')
    return data