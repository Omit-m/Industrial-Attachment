from functools import *

def add (a,b):
    return a+b

numbers= [2,4,5,6,7,8,5,9,7]

result=reduce(add,numbers)

print(result)