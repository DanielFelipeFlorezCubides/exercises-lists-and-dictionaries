from tabulate import tabulate
import os
from menu.firstExercises import firstlistDesign, firstdictDesign
from menu.fourthExercises import fourthListDesign, fourthDicDesign
from menu.secondExercises import secondListDesign, secondDicDesign
from menu.thirdExercises import thirdListDesign, thirdDicDesign
from menu.fifthExercises import fifthLista, fifthDiccionario
from menu.sixthExercises import sixthList, sixthDic

def designPrincipal():
    print("""
    ========================================
                  MAIN MENU
    ========================================
    1. List's Exercises
    2. Dictionarie's Exercises
    3. Exit
    """)
    return int(input("Choose an option (1-3): "))

def designList():
    print("""
    ========================================
            LIST'S EXERCISES MENU
    ========================================
    1. Exercise 1
    2. Exercise 2
    3. Exercise 3
    4. Exercise 4
    5. Exercise 5
    6. Exercise 6
    """)
    return int(input("Choose an option (1-6, other number to return to the main menu): "))

def designDict():
    print("""
    ========================================
           DICTIONARIE'S LIST MENU
    ========================================
    1. Exercise 1
    2. Exercise 2
    3. Exercise 3
    4. Exercise 4
    5. Exercise 5
    6. Exercise 6
    """)
    return int(input("Choose an option (1-6, other number to return to the main menu): "))

while True:
    match designPrincipal():
        case 1:
            while True:
                option = designList()
                match option:
                    case 1: os.system("clear"); firstlistDesign()
                    case 2: os.system("clear"); secondListDesign()
                    case 3: os.system("clear"); thirdListDesign()
                    case 4: os.system("clear"); fourthListDesign()
                    case 5: os.system("clear"); fifthLista()
                    case 6: os.system("clear"); sixthList()
                    case _: os.system("clear"); break
        
        case 2:
            while True:
                option = designList()
                match option:
                    case 1: os.system("clear"); firstdictDesign()
                    case 2: os.system("clear"); secondDicDesign()
                    case 3: os.system("clear"); thirdDicDesign()
                    case 4: os.system("clear"); fourthDicDesign()
                    case 5: os.system("clear"); fifthDiccionario()
                    case 6: os.system("clear"); sixthDic()
                    case _: os.system("clear"); break
        case 3:
            exit()