spam = ['apples', 'bananas', 'tofu', 'cats']
double = [0, 2]
third = ['some', 25, True]
empty = []

def create_list(items):
    if len(items) == 0:
        return 'Empty list'
    elif len(items) == 1:
        return str(items[0])
    elif len(items) == 2: 
        return str(items[0]) + ' and ' + str(items[1])
    else: 
        new_list = ''
        for i in items[:-2]:
            new_list += str(i) + ', '
        return new_list + str(items[-2]) + ' and ' + str(items[-1])
        
print(create_list(spam))
print(create_list(double))
print(create_list(third))
print(create_list(empty))