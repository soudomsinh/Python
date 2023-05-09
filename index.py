
# height = int(input("Enter your height: "))


# if age >= 13 and age <= 18:
#     print("You are teenager")
# elif age >= 19 and age <= 20 :
#     print("You are adolescent")
# elif age >= 21 and age <= 70:
#     print("You are adult working")
# elif age >= 71 :
#     print("You are retired")
# else:
#     print("You dont exist")


# nested if statement
# if height >=120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?: "))
#     if age <= 12 :
#         print("your ticket is $5")
#     elif age <=18:
#         print("Your ticket is $8")      
#     else:
#         print("Your ticket is $12")
# else:
#     print("Sorry you have to be taller")

# number = int(input("Enter your number: "))
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")


# variable1 = "John Doe"
# if variable1.startswith("John"):
#     print("Correct")
# else:
#     print("Wrong")

# variable2 = "12234"

# if variable2.endswith("244"):
#     print('Correct')
# else:
#     print('Wrong')

# temperature converter

# temp = input("Enter temperature in degree (C): ")

# degree = int(temp[:-1])
# unit = temp[-1].upper()

# print(degree, "=", unit)

# if unit == "C":
#     result = (degree) * 9/5 +32
#     unit_result = "Fahreinheit"
# elif unit == "F":
#     result= int(degree-32)*5/9
#     unit_result = "Celsius"

# print("Coverting = ",temp, "to", unit_result, " = ", result )

# While Loop
'''
while expression:
    statement

'''

i = 1
summation = 0
while i <=5:
    summation +=i 
    print("Value of sum = ", summation)
    i+=1 #1, 2,3,4,5
print("total summation is = ", summation)
