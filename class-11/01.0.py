def func(value):
    if isinstance(value , str):
        value = value + " this is imported!"
    elif isinstance(value, int):
        value = value ** 2
    else:
        raise NotImplementedError("This  operation could not be done!")

    return value


p = func("Bangladesh")
print(p)


q = func(10)
print(q)

func([1,2,3])