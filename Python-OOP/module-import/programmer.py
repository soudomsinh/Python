from employee import Employee

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