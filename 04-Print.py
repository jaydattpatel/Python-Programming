''' 
author : Jaydatt
print function
'''
print('-------------1-----------------')
print('Hello" World !' , 2023 )
print("Hello ' World !")
print("""" Hello " 
      ' World !'""")
print('''" Hello "  
      World !''')
print('int : ', 10)
print('float : ',3.14)
print("2**3 :",2**3)

print('-------------2-----------------')

x = 2
y = 6
print(f'sum of {x} and {y} is {x+y}; product: {x*y}.')

'''
(string with {}....).format(ele1,ele2,.....)
For two decimal places, put :.2f
'''

print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

print('-------------3-----------------')

val = 3.145131
print("Pi : {:.2f}".format(val))
print('-------------4-----------------')

names = ["Alexey", "Catalina", "Misuki", "Pablo"]

print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(f_three = names[3], first = names[1], f_one = names[0], f_two = names[2]))

# error : 'The set is {​{​{}, {}​}​}.'.format(a, b)

print('-------------5-----------------')

# %d for signed decimal numbers
# %u for unsigned decimal numbers
# %c for characters
# %f for floating-point real numbers
# %s for strings 
string = 'Welcome'
year = 2024
print('%s Python %d'%(string, year))
print('Python %c'%(year))
print('Python %u'%(year))
print('Python %f'%(year))