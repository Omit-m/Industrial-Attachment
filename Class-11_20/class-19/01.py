def is_valid_email(email: str):
    return email.endswith("gmail.com")


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


p1 = Person(name="nahid", email="dbc@gmail.com")

print(is_valid_email(p1.email))
