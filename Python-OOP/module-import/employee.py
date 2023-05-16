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

    
    def _getIncome(self, commission=0):
        return (self.__salary * 12) + commission
    
    def __str__(self):
        return ("Employee name = {},  Salary = {}, Department = {}, Annual Income = {} ".format(self.__name, self.__salary, self._department, self._getIncome()))

