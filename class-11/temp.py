from functools import singledispatch

@singledispatch
def func(value):
    pass

@func.register(str)
def _(value):
    value = value + " this is imported!"
    return value

@func.register(int)
def _(value):
    value = value ** 2
    return value


print( func(10) )
print( func("BD ") )