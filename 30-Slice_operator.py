'''
author : Jaydatt
The slice operator [n:m] returns the part of the string starting with the character at index n and go up to but not including the character at index m. Or with normal counting from 1, this is the (n+1)st character up to and including the mth character.

If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string.
'''
string = 'Welcome to python'
list = ['aa','bb','cc','dd']
tuple = (1, 2, 5, 3, 6, 4, 7, 2 ,2)

print('string[0:2] : ', string[0:2])
print('list[0:2] : ', list[0:2])
print('tuple[0:2] : ', tuple[0:2])

print('string[2:] : ', string[2:])
print('list[2:] : ', list[2:])
print('tuple[2:] : ', tuple[2:])

print('string[:2] : ', string[:2])
print('list[:2] : ', list[:2])
print('tuple[:2] : ', tuple[:2])

print('string[1:-1] : ', string[1:-1])
print('list[1:-1] : ', list[1:-1])
print('tuple[1:-1] : ', tuple[1:-1])

set = {'AA','BB','CC','DD'}
#print(set[0:2]) //error : not applicable for set

