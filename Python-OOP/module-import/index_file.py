from accountant import Accountant
from programmer import Programmer
from sale import Sale

account = Accountant("Sophie", 3000, 30)
print(account.__str__())
print("Commission = " + str(account._getIncome(1500)))
# print("Total Earning = " + str(account._getIncome))
programmer = Programmer("Neo", 7000, 3, "Game Development, Data Science")
print(programmer.__str__())
sale = Sale("John", 2500, "New York")
print(sale.__str__())
