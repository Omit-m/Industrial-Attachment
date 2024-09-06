"""
Access modifier;
    1) public (variable_name | method_name)
    2) protected (_variable_name | _method_name) -> later in INHERITENCE
    3) private (__variable_name | __method_name)
"""


class Person:
    def __init__(self, name, email, salary, age):
        # public attribute
        self.name = name
        self.email = email

        # private attribute
        self.__salary = salary

        # protected attribute
        self._age = age


p1 = Person(name="nahid", email="dbc@gmail.com", salary=20000, age=20)

# pubic
print(p1.name)

# error
# print(p1.__salary)

# valid
print(p1.__dict__.get("_Person__salary"))


print(p1._age)
