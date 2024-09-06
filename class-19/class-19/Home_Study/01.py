class Person:
    def __init__(self, name, number, age, salary):
        self.name = name
        self.number = number
        self.__age = age
        self.__salary = salary

    # Getter method to access the private attribute __age
    def get_age(self):
        return self.__age

    # Getter method to access the private attribute __salary
    def get_salary(self):
        return self.__salary

    # Method to update the private attribute __age
    def update_age(self, New_age):
        self.__age = New_age  # Corrected the assignment

# Creating an instance of the Person class
persons = Person("Omit", "0187****199", 21, 20000)

# Printing initial details
print(f"Name: {persons.name}\nNumber: {persons.number}\nAge: {persons.get_age()}\nSalary: {persons.get_salary()}")

# Updating the age
persons.update_age(New_age=25)

# Printing updated details
print(f"\nUpdated Age: {persons.get_age()}")
