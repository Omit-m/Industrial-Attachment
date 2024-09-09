def some_function(n):
    sum = 0
    for i in range(1,n):
        sum += i
    print("Sum is = ", sum)
    return sum

def my_simple_decorator(func):
    def wrapper(number):
        print("func called")
        func(number)
        print("func finished")
    return  wrapper

decorator = my_simple_decorator(some_function)

decorator(10)
decorator(15)

