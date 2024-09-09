# Magic method / DUNDER Method
import random


class Person:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.__salary = salary

    def __str__(self):
        return f"Person name is {self.name}"

    def __eq__(self, value: object) -> bool:
        return self.__salary == value.__salary

    def __gt__(self, value: object) -> bool:
        return self.__salary > value.__salary

    def __hash__(self) -> int:
        return random.randint(1, 10000)


p1 = Person(name="nahid", email="dbc@gmail.com", salary=30000)
p2 = Person(name="jahid", email="dec@gmail.com", salary=20000)

print(p1)
print(p2)

print(p1 == p2)

print(p1 > p2)


print(hash(p1))
print(hash(p2))
