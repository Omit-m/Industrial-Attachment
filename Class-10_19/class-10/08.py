def some_function(n):
    sum = 0
    for i in range(1,n):
        sum += i
    print("Sum is = ", sum)
    return sum

def hello():
    print("hi")

def something(a , b):
    print(f"a = {a} , b= {b}")

def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("func called")
        func(*args, **kwargs)
        print("func finished")
    return  wrapper

decorator = my_simple_decorator(some_function)
decorator(10)

decorator2 = my_simple_decorator(hello)
decorator2()

decorator3 = my_simple_decorator(something)
decorator3(b=1 ,a=2)
