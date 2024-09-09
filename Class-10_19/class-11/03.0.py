# without wrapper

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is the original function's docstring."""
    return "Hello, world!"

print(my_function.__name__)  # Output: wrapper
print(my_function.__doc__)   # Output: None
