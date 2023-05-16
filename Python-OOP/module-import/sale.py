from employee import Employee

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
    