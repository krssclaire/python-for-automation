def collatz(number):    
    if number % 2 == 0:
        result = number // 2 
    else:
        result = 3 * number + 1 
    print(result, end=' ')
    return result

# input validation
try:
    n = int(input('Inert integer number: '))
    while n != 1:
        n = collatz(n) 
except ValueError:
    print('Error: insert integer')