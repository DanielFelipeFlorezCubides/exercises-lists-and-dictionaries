# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
# donde <asignatura> es cada una de las asignaturas de la lista.
from logic.secondExercises import subjects_List, splitting

def design():
    subject = input('Please type the subject you wanna storage: ')
    subjects_List(subject)
    splitting()
    return 0
