# Escribir un programa que pregunte al usuario los números ganadores de la lotería 
# primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.
from logic.fourthExercises import lottery, format_date

def fourthListDesign():
    number = int(input('Please type a number between (1-100): '))
    print(lottery(number))
    return 0

# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
# y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa 
# donde <mes> es el nombre del mes.

def fourthDicDesign():
    date = input(('Please type the current date dd/mm/aaaa: '))
    print(format_date(date))
    return 0