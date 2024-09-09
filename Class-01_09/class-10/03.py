def outer():
    print("I am outer")
    def inner():
        print("I am inner")
    return inner

one = outer()

print(one)
one() #invoke
