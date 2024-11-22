# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas 
# que el usuario tiene que repetir.
from tabulate import tabulate
from logic.sixthExercises import failed_subject, read_file, write_file, update, show

def sixthList():
    
    failed= []

    subject = input(f" name of the Subject? : ")
    note = float(input(f"final Score of {subject}? : "))
    
    if note < 60:
        failed.append({"subject": subject, "note": note})
        failed_subject(subject, note)
    data = read_file("sixthExercisesList.json")
    
    if "subject" in data and "finalNote" in data:
        for subject, note in zip(data["subject"], data["finalNote"]):
            if note <60:
                failed.append({"subject" :subject, "note": note})
    
    if failed:
        headers = ["SUBJECT", "NOTE"]
        table_notes = [(epicfail['subject'], epicfail['note']) for epicfail in failed]
        print( "\n You must retake these subjects :")
        print(tabulate(table_notes, headers=headers, tablefmt="grid"))
    else:
        print("no failed Subjects.")

#Escribir un programa que cree un diccionario vacío 
# y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
# que se le pida al usuario. Cada vez que se añada 
# un nuevo dato debe imprimirse el contenido del diccionario.

def sixthDic():   
    data = read_file("sixthExercisesDic.json")

    while True:
        key = input("Fill the field with(name, age, gender) or 'exit' to finish: ").lower()
        if key == "exit":
            print("\nSaving and exiting...")
            write_file(data, "sixthExerciseDic.json")
            break

        value = input(f"Enter the value for {key}: ").strip()
        data = update(data, key, value)
        show(data)