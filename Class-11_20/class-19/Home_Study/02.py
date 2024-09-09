class person:
    def __init__(self, name, number, age, salary):
        self.name = name
        self.number = number
        self.age = age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, New_salary):
        self.__salary = New_salary


z = person(name="Omit", number="018*****99,", age=20, salary=20000)
print(f"Name: {z.name}\nNumber: {z.number}\nAge: {z.age}\nSalary: {z.salary}")
print("___________________________")
z.salary =25000

print(f"Name: {z.name}\nNumber: {z.number}\nAge: {z.age}\nSalary: {z.salary}")
