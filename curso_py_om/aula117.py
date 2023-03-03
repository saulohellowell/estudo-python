#function multiply  by 2, 3, 4 which item of list 

import random


result_2 = []
result_3 =[]
result_4 = []
z = []

def parametro(x,y,z):
    
    for item in z:
        x.append(item*y)
    
def numeros(z):
    z.append(random.sample(range(1,101),4))
    return z

numeros(z)
parametro(result_2,2,*z)
parametro(result_3,3,*z)
parametro(result_4,4,*z)

print (result_2)
print (result_3)
print (result_4)
