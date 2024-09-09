class Person:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.__salary = salary

    def get_salary(self):
        return self.__salary


p = Person(name="nahid", email="dbc@gmail.com", salary=20000)

print(p.get_salary())
