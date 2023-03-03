import math
from math import prod


def mult(*arg):
    
    return(prod(arg))
    
valor_final = mult(1,2,3,4,5)
print(valor_final)

def resto(x):
    if x % 2 == 0:
        return True
    else:
        return False   

def print_result(y):
    if y is True:
        print('par')
    else:
        print('impar')

print_result(resto(valor_final))



