# Getter & Setter approach


class Person:
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.__salary = salary

    # getter
    def get_salary(self):
        return self.__salary

    # setter
    def set_salary(self, new_salary, bonus=False):
        if new_salary < 10000:
            raise ValueError("Couldn't set salary under 10k")

        if bonus:
            self.__bonus_calculator()
        else:
            self.__salary = new_salary

    def __bonus_calculator(self):
        self.__salary += (self.__salary * 10) / 100


p = Person(name="nahid", email="dbc@gmail.com", salary=200000)

# p.name = 'jahid'

# set
p.set_salary(new_salary=25000)

# get
print(p.get_salary())

p.set_salary(new_salary=25000, bonus=True)
print(p.get_salary())

p.set_salary(new_salary=50000)
