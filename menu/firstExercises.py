from logic.firstExercises import storage_course, search_currency

def listDesign():
    course = input('Please type the course you want to storage: ')
    result = storage_course(course)
    print(result)

def dictDesign():
    currency = input('Please type the currency name: ')
    print(search_currency(currency))