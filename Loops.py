
'''
author : Jaydatt
Loops : for, while,
'''
print("for loop-----1------: ")
for i in range(3):
    print(i * 10)
    print(i + 10)

print("for loop-----2------: ")
for i in range(2,5):
    print(i * 10)
    print(i + 10)

print("for loop-----3------: ")
str = 'Welcome'
for char in str :
    print(char)

print("for loop-----4------: ")
lst = ['C','C++','Java','Python']
for language in lst :
    print('I learn' , language)

print("for loop-----5------: ")
set = {'C','C++','Java','Python'}
for language in set :
    print('I learn' , language)

print("for loop-----6------: ")
dictionary = {'Paul': 'Resnick', 'Brad': 'Miller', 'Lauren': 'Murphy'}
for key in dictionary:
    print("key :", key, ", val :",dictionary[key])

print("for loop-----7------: ")
tuple = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]
for first_name, last_name in tuple:
    print("first :", first_name, ", last :", last_name)


print("while loop-----1------: ")
i = 0
sum = 0
while(i <= 10) :
    sum += i
    i += 1
print("sum of 10 nums :" , sum)
