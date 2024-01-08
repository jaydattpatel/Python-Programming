''' 
author : Jaydatt
function syntax:

def function_name(arg1,arg2,....) :
   statement..1..
   statement..2..


'''
def square(x):
   return (x * x)

def sub(x, y):
   return (x - y)

print(square)
print(square(3))
print(sub(6, 4))

# return immutable tuple
def circleInfo(r):
    cir = 2 * 3.14159 * r
    area = 3.14159 * r * r
    return cir, area # return immutable tuple
   # or return (cir, area)
print(circleInfo(10))
circumference, area = circleInfo(10)
print(circumference)
print(area)

# return mutable list
def circleInfo(r):
    cir = 2 * 3.14159 * r
    area = 3.14159 * r * r
    return [cir, area] # return mutable list

print(circleInfo(10))
circumference, area = circleInfo(10)
print(circumference)
print(area)