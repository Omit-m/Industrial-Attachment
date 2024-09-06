class Person :
    """
    A class to represent a person with private attributes for age and salary.
    """

    def __init__(self, name, number, age, salary):
        """
        Initializes a new Person instance.

        Parameters:
        name (str): The name of the person.
        number (str): The contact number of the person.
        age (int): The age of the person.
        salary (float): The initial salary of the person.
        """
        self.name = name
        self.number = number
        self.__age = age
        self.__salary = salary

    def get_age ( self ) :
        """
        Gets the age of the person.

        Returns:
        int: The age of the person.
        """
        return self.__age

    def get_salary(self):
        """
        Gets the salary of the person.

        Returns:
        float: The salary of the person.
        """
        return self.__salary

    def update_age(self,New_age):
        """
        Updates the age of the person.

        Parameters:
        New_age (int): The new age to set for the person.
        """
        self.__age = New_age

    def set_salary(self, New_salary, bonus = False):
        """
        Sets the salary of the person, with an optional bonus.

        Parameters:
        New_salary (float): The new salary to set for the person.
        bonus (bool): If True, a 15% bonus is applied to the new salary.

        Raises:
        ValueError: If New_salary is less than 10,000.
        """
        if New_salary < 10000:
            raise ValueError("Couldn't set salary under 10k" )

        if bonus :
            self.__salary = New_salary  # Set the new salary first
            self.__bonus_calculator()  # Apply the bonus calculation
        else :
            self.__salary = New_salary

    def __bonus_calculator(self):
        """
        Private method to calculate a 15% bonus on the salary.
        """
        self.__salary += (self.__salary * 15) / 100


# Creating an instance of the Person class
persons = Person("Omit", "0187****199", 21, 20000)

# Printing initial details
print(f"Name: {persons.name}\nNumber: {persons.number}\nAge: {persons.get_age ( )}\nSalary: {persons.get_salary ( )}")
print("_____________________________________________________________________________")

# Updating the age and setting the salary with bonus
persons.update_age ( New_age = 25 )
persons.set_salary ( New_salary = 25000 , bonus = True )

# Printing updated details
print (
    f"Name: {persons.name}\nNumber: {persons.number}\nAge: {persons.get_age ( )}\nSalary: {persons.get_salary ( )}" )
