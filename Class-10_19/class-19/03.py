class Person:
    def __init__(self, name, email):
        # object attribute
        self.name = name
        self.email = email

    # object method
    def is_valid_email(self):
        return self.email.endswith("gmail.com")


p1 = Person(name="nahid", email="dbc@gmail.com")
print(p1.is_valid_email())

# value change of an attribute
p1.name = "jahid"
print(p1.name)
