# Creating class -> Employee()
class Employee():
    # Creating method -> detail()
    def detail(self, name, salary, department):
        self.name = name                    # this is attribute
        self.salary = salary                 # this is attribute
        self.department = department          # this is attribute
        print("Name = ", name)
        print("Salary = {} ".format(self.salary)) # Another way to do it
        print("Department = ", department)

# creating object -> obj1
obj1 = Employee()
obj1.detail("John", 5000, "IT" )


obj2 = Employee()
obj2.detail("Sara", 4000, "Accounting" )

obj3 = Employee()
obj3.detail("Tommy", 3000, "Designer" )
