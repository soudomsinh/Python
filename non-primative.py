# # primative data type
# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

# print(a,b,c,d,e)
# # non-primative: list
# number = [1,2,3,4,5,6]
# print(number[0])
# name  = ["John Doe", "Sara Smith"]
# print(name[0])

# mix_data = [10, "John Doe", True, 3.14, -10] # mixing type of data inside list
# print(mix_data[3])
# print(type(mix_data[3]))
# print(type(mix_data))

# How to edit/append new data into list
number2 = [1,2,3,4,5,6,7,8,9,10]

# print("before appending", number2)
# number2[2] = 9
# number2[4] = 18
# number2[-1] = "John"
# print("After appending", number2) # Now, number 9 replaced number 3 and 18 replaced 5 and John replaced 8

sum = 0
for x in number2:
    # print("List value of x =  ", x)
    sum += x
print(sum)
# checking 
if 20 in number2:
    print("yes, exist")
else:
    print("this number does not exist")


fruits = ["Mango", 'lemon', 'Apple']
if "Apple" in fruits:
    print("Yes, this fruits exist in list")
else:
    print("No, it does not exist")

# checking length of list
print(len(fruits)) # output:3





