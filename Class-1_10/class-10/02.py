# Higher Order Function (ex-1) -> Function as  a parameter

def square(num):
    return num ** 2

def qaud(num):
    return num ** 4

def helper(function_name, number):
    result = function_name(number)
    print("Your result " , result)


helper(qaud, 6)  # quad(6)
helper(square, 10) #  square(10)