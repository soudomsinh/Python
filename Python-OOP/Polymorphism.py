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
        return ("Employee name = {},  Salary = {}, Department = {}, Annual Income = {} ".format(self.__name, self.__salary, self._department, self._getIncome()))


# Subclass
class Accountant(Employee):
    _departmentName = "Accounting"
    def __init__(self, name, salary, age):
        super().__init__(name, self._departmentName, salary)
        self.__age = age
        
    def _showData(self): 
        super()._showData()
        print("Age =  " + str((self.__age)))
        print("#################################")

    def __str__(self):
        return (super().__str__() + ", Age = {} ".format(self.__age))



class Programmer(Employee):
    _departmentName = "Programmer"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name,  self._departmentName, salary)
        self.__exper = experience
        self.__skill = skill
        
    def _showData(self): 
        super()._showData()
        print("Experience = ". str(self.__exper))
        print("Skill(s) =  " + (self.__skill)) 
        print("#################################")

    def __str__(self):
        return (super().__str__() + "Exeperience = {} year(s), Skill = {} ".format(self.__exper, self.__skill))
        

class Sale(Employee):
    _departmentName = "Sale"
    def __init__(self, name, salary, area_responsibility): 
        super().__init__(name, self._departmentName, salary)
        self.__area = area_responsibility
        # super()._showData()
    def _showData(self): 
        super()._showData()
        print("Area of responsibility = " + (self.__area)) 
        print("#################################")

    def __str__(self):
        return (super().__str__() + ", Area of responsibilty = {} ".format(self.__area))
    

account = Accountant("Sophie", 3000, 30)
print(account.__str__())
programmer = Programmer("Neo", 7000, 3, "Game Development, Data Science")
print(programmer.__str__())
sale = Sale("John", 2500, "New York")
print(sale.__str__())



