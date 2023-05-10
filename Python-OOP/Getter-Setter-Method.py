'''
# Setter defines values TO Object

def setName(self, newName):
    self.__name=newname 

    
# Getter pulling values FROM Object

def getName(self):
    return self.__name


'''

# Access Modifier Level: Private
class Employee3(): 

    def __init__(self, name, department,salary):
        # Below are private attribute
        self.__name = name                    
        self.__department = department       
        self.__salary = salary               


    def _showData3(self): # _showData is a protected attribute
        print("name = {} ".format(self.__name)) 
        print("Department = {} ".format(self.__department)) 
        print("Salary = {} ".format(self.__salary)) 

# Setter method
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, newdepartment):
        self.__department = newdepartment


# Getter method
    def getName(self):
        return self.__name
    
    def getDepartment(self):
        return self.__department
    
    def getSalary(self):
        return self.__salary

# printing result for Setter method
# obj3 = Employee3("Tommy", "Manager",  7000) 
# obj3.__name = "Christopher"
# obj3.__department = "President"
# obj3.__salary = 10000
# obj3.setName("Christopher")
# obj3.setSalary(10000)
# obj3.setDepartment("President")
# obj3._showData3()



''''
output:

name = Christopher  # name get modified to Christopher 
Department = President   # Department get modified to President from Manager
Salary = 10000   # Salary get modified to 10,000 because it's private with two underscores

'''


# printing result for Getter method
obj3 = Employee3("Tommy", "Manager",  7000) 
print(obj3.getName())
# or we can print it out with text
print("The best employee of the year is :", format(obj3.getName()))
print("Department he works at is :", format(obj3.getDepartment()))
print("His salary is :", format(obj3.getSalary()))


''''
Output:
The best employee of the year is : Tommy
Department he works at is : Manager
His salary is : 7000

'''



   

