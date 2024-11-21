# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, 
# y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una des las asignaturas 
# de la lista y <nota> cada una de las correspondientes notas introducidas 
# por el usuario.
from logic.thirdExercises import subjects_List, grades
def design():
    subject = input('Please type the subject you wanna storage: ')
    grade = int(input('Please type the grade you scored on this subject: '))
    subjects_List(subject)
    return 0