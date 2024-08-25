''' 
author : Jaydatt
Asterisk Operator:

Multiplication Operator: *
Exponentiation Operator: **
Pack or Unpack Arguments : *args
Variable-Length Keyword Arguments : **kwargs
'''


print('-------Exponentiation-------')
# using asterisk
result = 5 ** 3
print(result)

print('-------Pack Arguments-------')
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1, 2, 3)  # Output: 1 2 3

print('-------Unpack Arguments-------')
def add(x, y):
    return x + y

numbers = (5, 7)
result = add(*numbers)  # result will be 12

print('-------Extended Iterable Unpacking-------')
first, *middle, last = [1, 2, 3, 4, 5]
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5

print('-------Variable-Length Keyword Arguments-------')
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Alice', age=30)  
# Output: name: Alice \n age: 30
