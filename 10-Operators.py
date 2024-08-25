
'''
author : Jaydatt
Arithmetic Operators (+, -, *, /, // ,% etc.)
Assignment Operators (=, +=, -=, etc.)
Comparison Operators (==, >=, <=, >, <, !=, etc.) (a < x < b)
Logical Operators (and, or, not)
'''
a = 10
b = 2

print('Arithmetic Operators:')

print('10+2:',10+2)    # sum
print('10-2:',10-2)    # sub
print('10*2:',10*2)    # mul
print('10/2:',10/2)    # div
print('10%2:',10%2)    # remender

print('Assignment Operators:')

print('if value of a is 10 then')
a = 10
a += 2
print('a+=2=',a )

a = 10
a /= 2
print('a/=2=',a)

print('2 ** 3 ** 2 =',2 ** 3 ** 2);     # the right-most ** operator gets done first!
print('(2 ** 3) ** 2 =',(2 ** 3) ** 2);   # use parentheses to force the order you want!
print('9 / 5 =',9 / 5)
print('9 // 5 =',9 // 5); # '//' use to truncate floating point
print('7.0 / 3.0 =',7.0 / 3.0)
print('7.0 // 3.0 =',7.0 // 3.0)
print('7.0 // 3 =',7.0 // 3)
print('16 - 2 * 5 // 3 + 1 =',16 - 2 * 5 // 3 + 1)


print('Comparison Operators:')
print('(15<5) : ',(15<5))
print('(15<=5) : ',(15<=5))
print('(15>=5) : ',(15>=5))
print('(10>5>1) : ',(10>5>1))
print('(10<5>1) : ',(10<5>1))

print('Logical Operators:')
bit1 = True
bit2 = False
print('(bit1 and bit2) :', (bit1 and bit2))
print('(bit1 or bit2) : ', (bit1 or bit2))
print('(not bit1) : ', (not bit1))
print('(not bit2) :', (not bit2))