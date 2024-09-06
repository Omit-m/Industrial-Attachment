class Person:
    def __init__(self, name, number, age, salary):
        self.name = name
        self.number = number
        self.__age = age
        self.__salary = salary


    def get_age(self):
        return self.__age


    def get_salary(self):
        return self.__salary


    def update_age(self, New_age):
        self.__age = New_age


    def set_salary(self, New_salary, bonus=False):
        if New_salary < 10000:
            raise ValueError("Couldn't set salary under 10k")

        if bonus:
            print(self.__salary)
            self.__salary = New_salary
            print ( self.__salary )
            self.__bonus_calculator()
        else:
            self.__salary = New_salary

    # প্রাইভেট ফাংশন: ১৫% বোনাস অ্যাপ্লাই করবে
    def __bonus_calculator(self):
        self.__salary += (self.__salary * 15) / 100  # ১৫% বোনাস হিসাব করবে


# একটি Person অবজেক্ট তৈরি করা হলো
persons = Person("Omit", "0187****199", 21, 20000)


print(f"Name: {persons.name}\nNumber: {persons.number}\nAge: {persons.get_age()}\nSalary: {persons.get_salary()}")
print("_____________________________________________________________________________")

persons.update_age(New_age=25)
persons.set_salary(New_salary=25000, bonus=True)

print(f"Name: {persons.name}\nNumber: {persons.number}\nAge: {persons.get_age()}\nSalary: {persons.get_salary()}")
