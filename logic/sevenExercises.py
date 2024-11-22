#Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
#las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante.
from tabulate import tabulate
import json

def read_file(path):
    with open(f"databases/SevenExercises/{path}", "r") as file:
        data = file.read()
        convertirList = json.loads(data) 
        return convertirList
    
def write_file(data, path):
    with open(f"databases/SeventhExercises/{path}", "wb+") as file:
        convertirJson = json.dumps(data, indent=4).encode("utf-8")
        file.write(convertirJson)
        file.close()

def reset(path):
    with open(f"databases/SeventhExercises/{path}", "w") as file:
        json.dump({"alphabet": []}, file, indent = 4 )