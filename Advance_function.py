''' 
author : Jaydatt
Advance function : optional parameter and keyword parameter
'''

print("------Optional Parameters--1-----: ")
def add(v1=0,v2=0,v3=0):
    return (v1+v2+v3)

print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))


print("------Optional Parameters--2-----: ")
def fun(x = 1, y = 2, z = 3):
    return("X={} ; Y={} ; Z={}".format(x,y,z))

print("fun() : ",fun())
print("fun(1) : ",fun(1))
print("fun(1,2) : ",fun(1,2))
print("fun(1,2,3) : ",fun(1,2,3))

print("fun(x = 10) : ",fun(x=10))
print("fun(y = 20) : ",fun(y=20))
print("fun(z = 30) : ",fun(z=30))

print("fun(x = 10,y = 20) : ",fun(x=10,y = 20))
print("fun(y = 20,z = 30) : ",fun(y=20,z = 30))
print("fun(z = 30,x = 10) : ",fun(z = 30,x = 10))

print("fun(x = 10,y = 20,z = 30) : ",fun(x = 10,y = 20,z = 30))
print("fun(y = 20,x = 10,z = 30) : ",fun(y = 20,x = 10,z = 30))
print("fun(z = 30,y = 20,x = 10) : ",fun(z = 30,y = 20,x = 10))


print("------Optional Parameters--3-----: ")
print(int("100"))
print(int("100", 10))   # same thing, 10 is the default value for the base
print(int("100", 8))     # now the base is 8, so the result is 1*64 = 64

print("------Optional Parameters--4-----: ")
def addList(val = "NA", lst = []):
    lst.append(val)
    return lst

print(addList())
print(addList(1))
print(addList("Py"))
print(addList(2))

print(addList(4, []))
print(addList(5, ["Hello"]))