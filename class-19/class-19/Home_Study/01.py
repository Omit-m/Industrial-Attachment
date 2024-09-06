class Person:
    def __init__(self, name, number, age):
        self.name = name
        self.number = number
        self.__age = age


    def gat_age(self):
        return self.__age


persons = Person("Omit", "01872035199", 21)

print(F"Name : {persons.name}\nNumber: {persons.number}\nAge : {persons.gat_age()}")