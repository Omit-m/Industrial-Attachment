from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function(name):
    """This is the original function's docstring."""
    return f"Hello {name}"

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is the original function's docstring.

print(my_function("sakib"))
print(my_function("nahid"))