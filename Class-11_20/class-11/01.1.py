from functools import singledispatch

# Create a dispatcher function
@singledispatch
def process(value):
    raise NotImplementedError("Unsupported type")

# Define behavior for integers
@process.register(int)
def _(value):
    return f"Handling an integer: {value}"

# Define behavior for strings
@process.register(str)
def _(value):
    return f"Handling a string: {value}"

# Usage
print(process(42))    # Outputs: Handling an integer: 42
print(process("hello"))  # Outputs: Handling a string: hello
