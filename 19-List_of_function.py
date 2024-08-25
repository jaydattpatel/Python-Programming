''' 
author : Jaydatt

You can even have a list of functions (!).

'''

def msg1():
    print('hello')
def msg2():
    print('world')
ll = [msg1,msg2] # creating list of function
ll[0]() # calling function
ll[1]() # calling function


def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("-------names-------")
for fun in L:
    print(fun)

print("-------call each of them-------")
for fun in L:
    print(fun(-2))

print("-------just the first one in the list-------")
print(L[0]) # get the details of function
print(L[0](3)) # parsing argument in function of list 


