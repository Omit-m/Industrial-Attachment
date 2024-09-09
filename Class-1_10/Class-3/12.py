person3 = {
    "name": "xyz",
    "age": 30,
    "email": "xyz@gmail.com",
    "marital_status": True,
    "experience": 5,
    "languages": ["Bangla", "English", "German"],
}

# Accesing Dictionary

# way:1 -> Bracket Notation
print(person3["name"])
print(person3["email"])

# way:2 -> .get()
print(person3.get("age"))

# better
# print(person3["salary"]) # error
print(person3.get("salary"))

# Dictiory of list
print(person3.get("languages"))
print(person3.get("languages")[1])


# Home work
"""
His name is xyz. He is 30 years of old. His email address is 'xyz@gmail.com'.
Is he married ? True. He has 5 years of experiens.
"""
