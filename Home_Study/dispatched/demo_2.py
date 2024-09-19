from functools import singledispatch

@singledispatch
def Handling(value):
    pass
@Handling.register(int)
def _(value):
    return (f"Handling integer : {value **2}")



print(Handling(1))


#
# from functools import singledispatch
#
# @singledispatch
# def Handling(value):
#     pass
#
# @Handling.register(int)
# def _(value):
#     return f"Handling integer: {value ** 2}"
#
# print(Handling(12))  # This will handle an integer
# print(Handling("12"))  # This will call the default function (which does nothing)
