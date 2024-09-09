# access these values and make the bio
# List of Dictionaries

persons = [
    {"name": "xyz", "age": 10, "email": "abc@gmail.com", "marital_status": False},
    {"name": "def", "age": 20, "email": "def@gmail.com", "marital_status": False},
    {
        "name": "xyz",
        "age": 30,
        "email": "xyz@gmail.com",
        "marital_status": True,
        "experience": 5,
    }
]

# print(type(persons)) # see TYPE

print(persons[0].get("age"))  # specific value  asses (.get("Value name")
print(persons[1])
print(persons[2])
