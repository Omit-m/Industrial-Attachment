def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("func called")
        func(*args, **kwargs)
        print("func finished")
    return  wrapper

@my_simple_decorator
def some_function(n):
    sum = 0
    for i in range(1,n):
        sum += i
    print("Sum is = ", sum)
    return sum

@my_simple_decorator
def hello():
    print("hi")

@my_simple_decorator
def something(a , b):
    print(f"a = {a} , b= {b}")


some_function(n=10)
hello()

