def some_function():
    print("Oh! You  called me ?")
    sum = 0
    for i in range(1,10):
        sum += i
    return sum

def my_simple_decorator(func):
    def wrapper():
        print("func called")
        func()
        print("func finished")
    return  wrapper

decorator = my_simple_decorator(some_function)

decorator()
decorator()
decorator()
decorator()
decorator()
decorator()

