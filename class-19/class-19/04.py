class Person:
    def __init__(self, name, email):
        # object attribute
        self.name = name
        self.email = email

    # object method
    def is_valid_email(self):
        return self.email.endswith("gmail.com")


p1 = Person(name="nahid", email="dbc@gmail.com")
# print(p1.__dict__)
p2 = Person(name="nahid", email="dbc@mail.com") #  output = False
print(p1.is_valid_email())
print(p2.is_valid_email())
# print(dir(p1))
