# property


class Person:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary


p = Person(name="nahid", email="dbc@gmail.com", salary=20000)

print(p.salary)
p.salary = 50000
print(p.salary)
