# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
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

def storage_course(course):
    data = read_file('firstExercisesList.json')
    data.append(course)
    write_file(data, 'firstExercisesList.json')
    return data

# Escribir un programa que guarde en una variable 
# el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo 
# o un mensaje de aviso si la divisa no está en el diccionario.

def search_currency(currency):
    data = read_file("firstExercisesDic.json")
    if data.get(currency):
        return data.get(currency)
    else:
        return 'Currency not found'