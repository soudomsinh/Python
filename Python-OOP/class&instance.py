''''
Class Variable & Instance variable

Class variable is the variable within class 

'''


# Access Modifier Level: Private
class Employee(): 
    # class variable
    _minSalary = 2000
    _maxSalary = 10000
    _companyName = "Smith Corp.Limited"
    def __init__(self, name, department,salary):
        # Below are instance variable
        self.__name = name                    
        self._department = department       
        self.__salary = salary               


    def _showData(self): # _showData is a protected attribute
        print("name = {} ".format(self.__name)) 
        print("Department = ",format(self._department)) 
        print("Salary = ",format(self.__salary)) 


# printing result for Setter method
obj = Employee("Tommy", "Manager",  7000) 
print("Minimum salary = ", Employee._minSalary)
print("Company = ", Employee._companyName)

# obj._showData()
