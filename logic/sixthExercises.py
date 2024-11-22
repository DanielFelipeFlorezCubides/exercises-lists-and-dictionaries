# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas 
# que el usuario tiene que repetir.

import json

def read_file(path):
    with open(f"databases/SixthExercises/{path}", "r") as file:
        data = file.read()
        convertirList = json.loads(data) 
        return convertirList
    
def write_file(data, path):
    with open(f"databases/SixthExercises/{path}", "w") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()
        
def failed_subject(course, note):
    data = read_file("sixthExercisesList.json")
    data["subject"].append(course)
    data["finalNote"].append(note)
    write_file(data, "sixthExercisesList.json")
    return data

#Escribir un programa que cree un diccionario vacío 
# y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada 
# un nuevo dato debe imprimirse el contenido del diccionario.

def update(data, key, value):
    data[key] = value
    return data

def show(data):
    print("\nData stored")
    for k, v in data.items():
        print(f"{k.capitalize()}: {v}")
    print()