'''
inheritance allows us to define a class that inherits all the methods and properties from another class. 
Parent class is the class being inherited from, also called base class. 
Child class is the class that inherits from another class, also called derived class.

Superclass ---> use when we want to 
Subclass   

class Person:        # Person is the superclass                
    name = ""  

    def __init__(self, personName):  
        self.name = personName  
  
    def showName(self):  
        print(self.name)  
  
class Student(Person):      # Student inherits from Person superclass
    studentClass = ""  

'''
 
class Employee():    # Superclass ---> parent class

    __minSalary = 2000
    maxSalary = 10000
    companyName = "Smith Corp.Limited"

    def __init__(self, name, department,salary):
        # Below are instance variable
        self.__name = name                    
        self._department = department       
        self.__salary = salary               


    def _showData(self): # _showData is a protected attribute
        print("name = {} ".format(self.__name)) 
        print("Department = ",format(self._department)) 
        print("Salary = ",format(self.__salary)) 

    def _getIncome(self):
        return self.__salary * 12
    
    def __str__(self):
        return ("Employee name = {},  Salary {}, Department = {}, Annual Income = {} ".format(self.__name, self.__salary, self._department, self._getIncome()))


# Subclass
class Accountant(Employee):
    _departmentName = "Accounting"
    def __init__(self, name, salary):
        super().__init__(name, self._departmentName, salary)
        # super()._showData()
        


class Programmer(Employee):
    _departmentName = "Programmer"
    def __init__(self, name, salary):
        super().__init__(name,  self._departmentName, salary)
        # super()._showData()
      

class Sale(Employee):
    _departmentName = "Sale"
    def __init__(self, name, salary): 
        super().__init__(name, self._departmentName, salary)
        # super()._showData()

    
#     pass




account = Accountant("Sophie", 3000)
# account._showData()
print(account.__str__())

sale = Sale("John", 2500)
# sale._showData()
print(sale.__str__())

programmer = Programmer("Neo", 7000)
# programmer._showData()
print(programmer.__str__())



# print(programmer.__minSalary) #AttributeError: 'Programmer' object has no attribute '__minSalary' bacause __minSalary is private
# print(programmer._Employee__minSalary) # this one works if desire to access private attribute
# print(programmer.maxSalary) # attribute is public
