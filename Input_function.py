''' 
author : Jaydatt
input function to get input from user as string
data of input always will be string.........
'''
# input function
''' receive the string or value by input '''

name = input("Enter the name:")    # data of input always will be string.........
print(type(name)) 


a = input("Enter the fist value:") # data of input always will be string.........
x = int(a)     # so we need to convert string to integer

b = input("Enter the second value:") # data of input always will be string.........
y = int(b)    # so we need to convert string to integer

z = (x + y)/2
print('Average valur of x and y is',z)


### Fix Enter Input in integer and float............
print('\nEnter Input in integer and float............')
m1 = int(input("Enter Marks1 in integer: "))
m2 = int(input("Enter Marks2 in integer: "))
m3 = float(input("Enter Marks3 in float: "))
m4 = float(input("Enter Marks4 in float: "))
myList = [m1, m2, m3, m4]
myList.sort()
print('\n',myList)