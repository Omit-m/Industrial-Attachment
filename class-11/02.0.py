from functools import reduce

# Function to add two numbers
def add(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]

# Use reduce to apply the add function cumulatively
result = reduce(add, numbers)

print(result)  
