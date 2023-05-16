'''
polymorphism is object's ability to take on multiple forms. 
The term is derived from two distinct terms: poly, which means numerous, 
and morphs, which means forms.

Overloading method vs Overriding method

'''
 
class Employee():    # Superclass ---> parent class

    __minSalary = 2000
    maxSalary = 10000
    companyName = "Smith Corp.Limited"

    def __init__(self, name, department,salary):
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
    def __init__(self, name, salary, age):
        super().__init__(name, self._departmentName, salary)
        self.__age = age
        
    def _showData(self): 
        super()._showData()
        print("Age = {} ".format(self.__age)) 
        print("#################################")

        


class Programmer(Employee):
    _departmentName = "Programmer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name,  self._departmentName, salary)
        self.__exper = experience
        self.__skill = skill
        # super()._showData()
    def _showData(self): 
        super()._showData()
        print("Experience = {} ".format(self.__exper), "year(s)") 
        print("Skill(s) = {} ".format(self.__skill)) 
        print("#################################")

      

class Sale(Employee):
    _departmentName = "Sale"
    def __init__(self, name, salary, area_responsibility): 
        super().__init__(name, self._departmentName, salary)
        self.__area = area_responsibility
        # super()._showData()
    def _showData(self): 
        super()._showData()
        print("Area of responsibility = {} ".format(self.__area)) 
        print("#################################")


account = Accountant("Sophie", 3000, 30)
account._showData()
sale = Sale("John", 2500, "New York")
sale._showData()
programmer = Programmer("Neo", 7000, 3, "Game Development, Data Science")
programmer._showData()


