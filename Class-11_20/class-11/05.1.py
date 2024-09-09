from functools import partial

def power(a,b):
    print("power calling..")
    return a**b

squared_function = partial(power, b=2)
print(squared_function(1))
print(squared_function(2))
print(squared_function(3))

cubic_function = partial(power, b=3)
print(cubic_function(1))
print(cubic_function(2))
print(cubic_function(3))


power(10,10)