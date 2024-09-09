def some_function():
    print("Oh! You  called me ?")
    sum = 0
    for i in range(1,10):
        sum += i
    return sum

def hello():
    print("Hi")

def my_simple_decorator(func):
    def wrapper():
        functioner_name = func.__name__
        print(f"{functioner_name} called")
        func()
        print(f"{functioner_name} finished")
    return  wrapper

decorator = my_simple_decorator(some_function)

decorator()
decorator()

decorator2 = my_simple_decorator(hello)

decorator2()
decorator()
decorator2()

