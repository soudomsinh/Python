# Constructor

# Creating class -> Employee()
class Employee():

    # Creating constructor
    def __init__(self, name, salary, department):
        self.name = name                    # this is attribute
        self.salary = salary                 # this is attribute
        self.department = department          # this is attribute

    def showData(self):
        print("name = {} ".format(self.name)) # Another way to do it
        print("Salary = {} ".format(self.salary)) # Another way to do it
        print("Department = {} ".format(self.department)) # Another way to do it


# creating object -> obj1, obj2, obj3

obj1 = Employee("John", 5000, "IT" ) # First object
obj2 = Employee("Sara", 4000, "Accounting" )  # Second Object
obj3 = Employee("Tommy", 3000, "Designer" )   # Third Object

# isinstance vs dir
print(isinstance(obj1, Employee)) # outpu: True because obj1 built from class Employee
print(isinstance(obj1, int)) # outpu: False because obj1 is not built from class Employee

# dir
print(dir(obj1))
print(dir(obj1.__class__))

