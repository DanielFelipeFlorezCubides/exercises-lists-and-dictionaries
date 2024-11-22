# Escribir un programa que almacene en una lista los números 
# del 1 al 10 y los muestre por pantalla en orden inverso 
# separados por comas.
from logic.fifthExercises import invert, notas, get
def lista():
    invert()

# Escribir un programa que almacene el diccionario con 
# los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después 
# muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, 
# donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también
# el número total de créditos del curso.

def diccionario():
    subject = input('Please type the subject you wanna storage: ')
    grade = int(input(f'Please type the grade you scored on {subject}: '))
    notas(subject, grade)
    total = get()
    print(f"The credit's sum is: {total}")
