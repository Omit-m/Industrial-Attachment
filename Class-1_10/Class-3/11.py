"""
Dictionary Syntax

{
    'key1' : value1,
    'key2' : value2,
    .,
    .,
    'keyN' : valueN,
}
"""

person1 = {
    "name": "xyz",
    "age" : 10,
    "email" : "abc@gmail.com",
    "marital_status" : False
}

person2 = {
    "name": "def",
    "age" : 20,
    "email" : "def@gmail.com",
    "marital_status" : False
}

# person3 = ["xyz", 30 , "xyz@gmail.com", True , 5 ]
person3 = {
    "name": "xyz",
    "age" : 30,
    "email" : "xyz@gmail.com",
    "marital_status" : True,
    "experience": 5
}

print(person3["name"])
print(type(person3))