# Escribir un programa que pregunte al usuario los números ganadores de la lotería 
# primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.
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

def lottery(number):
    data = read_file('fourthExercisesList.json')
    data.append(number)
    data.sort()
    write_file(data, 'fourthExercisesList.json')
    return data

# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa 
# donde <mes> es el nombre del mes.

def format_date(date):
    list = date.split('/')
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    data = read_file('fourthExercisesDic.json')
    formato = {
        'day': list[0],
        'month': months[int(list[1] - 1)],
        'year': list[2],
        'message': f'{list[0]} de {months[int(list[1] - 1)]} de {list[2]}'
    }
    data.sort()
    write_file(data, 'fourtExercisesDic.json')
    return 0