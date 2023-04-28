def lesson_2(*args):
    count = 0
    for finish in args:
        if len(finish) > count:
            count = len(finish)
    return print('Максимальне кількість символів в рядку:' , count)
lesson_2("Red" , "Finish" , "Value" , "Start")