from functools import *

def add(x,y):
    return x * y
numbers=[5,4,6,7,3,45,3,4,578,9]

result=reduce(add,numbers)

print(result)