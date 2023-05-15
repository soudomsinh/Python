'''
inheritance allows us to define a class that inherits all the methods and properties from another class. 
Parent class is the class being inherited from, also called base class. 
Child class is the class that inherits from another class, also called derived class.

Superclass ---> parent class
Subclass   ---> Child class

class Person:        # Person is the superclass                
    name = ""  

    def __init__(self, personName):  
        self.name = personName  
  
    def showName(self):  
        print(self.name)  
  
class Student(Person): 				# Student inherits from Person superclass
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


# Subclass
class Accountant(Employee):
    _departmentName = "Accounting"
    def __init__(self):
        pass
        # Below are instance variable
        # self.__name = name                    
        # self._department = department       
        # self.__salary = salary  

class Programmer(Employee):
    _department = "Programmer"
    def __init__(self):
        pass

class Sale(Employee):
    _departmentName = "Sale"
    def __init__(self):
        pass
#     pass




account = Accountant()
print(account.companyName)




# sale = Sale()


programmer = Programmer()
# print(programmer.__minSalary) #AttributeError: 'Programmer' object has no attribute '__minSalary' bacause __minSalary is private
print(programmer._Employee__minSalary) # this one works if desire to access private attribute
print(programmer.maxSalary) # attribute is public
