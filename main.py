def combine_dicts(*args):
    dictionary = {}
    for finish in args:
        dictionary.update(finish)
    return dictionary
print(combine_dicts({'Start' : '15' , 'finish' : 'red' , 'color' : 'yello'}))