'''
author : Jaydatt
count is used to count hom many time word is used 
index is used to find index number of matching word

count : The first method we'll talk about is called count. It requires that you provide one argument, which is what you would like to count. The method then returns the number of times that the argument occured in the string/list the method was used on. There are some differences between count for strings and count for lists. When you use count on a string, the argument can only be a string. 

index: The other method that can be helpful for both strings and lists is the index method. The index method requires one argument, and, like the count method, it takes only strings when index is used on strings, and any type when it is used on lists. For both strings and lists, index returns the leftmost index where the argument is found. If it is unable to find the argument in the string or list, then an error will occur.
'''
string = 'Welcome to python'
list = ['aa','bb','cc','dd', [] ]
tuple = (1, 2, 5, 3, 6, 4, 7, 2 ,2)

print("string.count('x') : ", string.count('x'))
print("list.count('jj') : ", list.count('jj'))
print("tuple.count(11) : ", tuple.count(11))

print("string.count('e') : ", string.count('e'))
print("list.count('bb') : ", list.count('bb'))
print("tuple.count(2) : ", tuple.count(2))

print("string.index('p') : ", string.index('p'))
print("list.index('cc') : ", list.index('cc'))
print("list.index([]) : ", list.index([]))
print("tuple.index(6) : ", tuple.index(6))

# error if word not match
# Error : print("string.index('x') : ", string.index('x'))
# Error : print("list.index('jj') : ", list.index('jj'))
# Error : print("tuple.index(11) : ", tuple.index(11))

set = {'AA','BB','CC','DD'}
# error:  print(set.count('AA')) not applicable for set