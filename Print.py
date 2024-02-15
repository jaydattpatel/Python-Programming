''' 
author : Jaydatt
print function
'''
print('Hello" World !' , 2023 )
print("Hello ' World !")
print("""" Hello " 
      ' World !'""")
print('''" Hello "  
      World !''')
print('int : ', 10)
print('float : ',3.14)
print("2**3 :",2**3)

course = "Python"
year = 2023

'''
(string with {}....).format(ele1,ele2,.....)
For two decimal places, put :.2f
'''
print("Welcome to {} in {}.".format(course,year))

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

val = 3.145131
print("Pi : {:.2f}".format(val))

names = ["Alexey", "Catalina", "Misuki", "Pablo"]

print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(f_three = names[3], first = names[1], f_one = names[0], f_two = names[2]))

 # error : 'The set is {​{​{}, {}​}​}.'.format(a, b)
