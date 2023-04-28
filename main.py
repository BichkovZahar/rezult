def lesson_4(*args):
    slovo = {}
    for key , value in args:
        slovo[key] = value
    return slovo
print(lesson_4(*[('Захар' , 15) , ('Женя' , 16) , ('Даша' , 17)]))