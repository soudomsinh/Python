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


# creating object -> obj1

# First object
obj1 = Employee("John", 5000, "IT" )
obj1.showData()
obj1.salary = 7000    # modifying value in class
obj1.name = "John Doe" # new value in class of name
obj1.department = "Manager" # new value in class of name

obj1.showData()

# Second Object
obj2 = Employee("Sara", 4000, "Accounting" )
obj2.showData()
obj2.name = "Sara Smith"
obj2.department = "Developer"
obj2.showData()

# Third Object
obj3 = Employee("Tommy", 3000, "Designer" )

# obj2.showData()
# obj3.showData()

