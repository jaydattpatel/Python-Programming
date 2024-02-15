# string

# Joint strings............

a = "Welcome to "
b = 'World'
print("concate:",a+b)

str_s0 = sorted(a+b)
print("Sorted:",str_s0)

print("len('ABCDE') : ",len('ABCDE'))
''' string slicing..............
A   B   C   D   E  
0   1   2   3   4 (print 0 to 4 means A-Z) 
-5  -4  -3  -2  -1 (print -5 to -1 means A-Z)  
'''

print('\nget string from forward positive index..........................')
str_a2z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(str_a2z[0:5])   
print(str_a2z[2:5])      
print(str_a2z[:3])     
print(str_a2z[3:])      

print ('\nget string from reverse negative index : ')
print(str_a2z[-5:-2])      
print(str_a2z[-5:-1])
print(str_a2z[:-3])       
print(str_a2z[-3:])  


# strings skip Index array............
print('\nstrings skip Index array......................................')
print(str_a2z[0:11:1])  # ger string with skip 1
print(str_a2z[0:11:2])  # ger string with skip 2
print(str_a2z[0:11:3])  # ger string with skip 3  

str_s1 = "Welcome To Python"
print('\nstr_s1.upper() : ',str_s1.upper())
print('str_s1.lower() : ',str_s1.lower())

# compare last characters of strings............
str_s2 = 'It is a good one story'
print( "\n'It is a good one story' is ending with 'story' :  ",str_s2.endswith("story"))

# find count of word used in strings............
str_s3 = 'It is a good one story. It is very intresting and story is too much old.' 
cnt1 = str_s3.count("is")
print( "\n'is' counted ",cnt1)


# make capitalize first character of strings............
str_s4 = 'good story.' 
print(str_s4)
print("\nstr_s4.capitalize() : ",str_s4.capitalize())

# find character or word in strings............(if value is 0 or grater then its exist, then it is -1 means not exist)
str_s5 = 'It is a good one story.'
print("\nstr_s5.find('good') : ",str_s5.find('good'))


# replace character or word in strings............
str_s6 = 'It is a very cheap.'  
str_s6 = str_s6.replace('very','so')
print("\nstr_s6.replace('very','so') : ",str_s6)


# split string into list form
str_s7 = 'It is a very cheap.'  
list = str_s7.split()
print("\nstr_s7.split() : ",list)

list = str_s7.split('a')
print("\nstr_s7.split('a') : ",list)
print('type(list)) : ',type(list))

# join list elements in string format
list1  = ['red','blue','green']
str_s8 = ';'
str_s9 = str_s8.join(list1)
print('\nstr_s8.join(list1) : ',str_s9)

# strip() to remove space in start and end of string
str_s10 = "     Hello World !      "
print("\nstr_s10.strip() : "+"**",str_s10.strip()+"**")

# comparison of value
a = "banana"
b = "banana"

print("\n(a is b) : ",(a is b))
print("(a == b) : ",(a == b))

print("id(a) : ",id(a))
print("id(b) : ",id(b))

'''
(string with {}....).format(ele1,ele2,.....)
For two decimal places, put :.2f
'''
course = "python"
year = 2024
print("Welcome to {} in {}.".format(course,year))

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

val = 3.145131
print("Pi : {:.2f}".format(val))

names = ["Alexey", "Catalina", "Misuki", "Pablo"]

print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format( f_three = names[3], first = names[1], f_one = names[0], f_two = names[2]))