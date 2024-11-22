# Escribir un programa que almacene en una lista los números 
# del 1 al 10 y los muestre por pantalla en orden inverso 
# separados por comas.

import json
def read_file(path):
        with open(f'dataBases/FifthExercises/{path}', 'r') as file:
            data = file.read()
            convertList = json.loads(data)
            return convertList
    
def write_file(data, path):
    with open(f'dataBases/FifthExercises/{path}', 'wb+') as file:
        convertJson = json.dumps(data, indent=4).encode('utf-8')
        file.write(convertJson)
        file.close()

def invert():
     data = read_file('fifthExercisesList.json')
     data.sort(reverse=True)
     write_file(data, 'fifthExercisesList.json')
     return print(data)

# Escribir un programa que almacene el diccionario con 
# los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después 
# muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también
# el número total de créditos del curso.

def notas(subject, credits):
    data = read_file('fifthExercisesDic.json')
    formato = {
         "Subject": subject,
         "Credit": credits,
         "Message": print(f"{subject} tiene {credits} creditos.")
    }
    data.append(formato)
    write_file(data, 'fifthExercisesDic.json')
    return formato['Message']

def get():
    data = read_file('fifthExercisesDic.json')
    subjectsDic = len(data)
    suma = 0
    print('Subjects list')
    for i in range(0, subjectsDic):
         credits = data[i]
         suma += credits["Credit"]
    return suma