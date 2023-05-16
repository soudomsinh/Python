from employee import Employee

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


