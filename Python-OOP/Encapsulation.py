'''
Encapsulation has three level of access modifier such as public, protected, and private
1. public meaning anyone and access and modify the values within and outside the class
2. protected meaning anyone can acess and modify values within and outside the class but with some limitation. Using one "_" (underscore)
3. private meaning NO one can access and modify the values inside class. Using two "__" (two underscores)


class Employee():
    def __init__(self, name,department,salary): # this a private attribute because there are two underscores in ```__init__```
        self.name = name            # this is a public attribute(Accessible within or outside of class)
        self._department = department    # this is a protected attribute(accessible within the class and sub-class)
        self.__salary = salary          #  This is a private attribute(Accessible only within a class)


'''
# Access Modifier Level: Public

class Employee1(): 

    def __init__(self, name, department,salary):
        # Below are public attribute
        self.name = name                    
        self.department = department       
        self.salary = salary               


    def showData1(self):
        print("name = {} ".format(self.name)) 
        print("Department = {} ".format(self.department)) 
        print("Salary = {} ".format(self.salary)) 


# obj1 = Employee1("John", "Programmer", 5000) # First object
# obj1.showData1()
# obj1.salary = 7000
# obj1.name = "Neo Anderson"
# obj1.showData1()

''''
output: salary = 7000 # value of salary get modified to 7000 from 5000
output: name = Neo Anderson # value of name can modified to Neo Anderson from John

'''

# Access Modifier Level: Protected
class Employee2(): 

    def __init__(self, name, department,salary):
        # Below are protected attribute
        self._name = name                    
        self._department = department       
        self._salary = salary               


    def _showData2(self):
        print("name = {} ".format(self._name)) 
        print("Department = {} ".format(self._department)) 
        print("Salary = {} ".format(self._salary)) 


# obj2 = Employee2("Sara", "Accountant", 4000 ) 
# obj2.name = "Joey"
# print(obj2._name)
# obj2._name = "Julia"
# print(obj2._name)
# obj2._salary = 10000
# obj2._showData2()

''''
output:
name = Sara 
Department = Accountant 
Salary = 4000 
Sara    # Name can't be modified. The output is still Sara because obj2.name = "Joey" (without underscore)
Julia
name = Julia   #Now, name get modified because an underscore (_) get added in front of _name
Department = Accountant  
Salary = 4000 # Salary get modified to 10,000

'''

# Access Modifier Level: Private
class Employee3(): 

    def __init__(self, name, department,salary):
        # Below are private attribute
        self._name = name                    
        self.__department = department       
        self.__salary = salary               


    def _showData3(self): # _showData is a protected attribute
        print("name = {} ".format(self._name)) 
        print("Department = {} ".format(self.__department)) 
        print("Salary = {} ".format(self.__salary)) 


# creating object -> obj1, obj2, obj3

obj3 = Employee3("Tommy", "Manager",  7000) 
obj3._name = "Christopher"
obj3.__department = "President"
obj3.__salary = 10000
obj3._showData3()


''''
output:

name = Christopher  # name get modified to Christopher 
Department =  Manager  #Department did not get modified to President because it's private with two underscores
Salary = 7000   # Salary did not get modified to 10,000 because it's private with two underscores

'''


   

