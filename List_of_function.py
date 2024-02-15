''' 
author : Jaydatt

You can even have a list of functions (!).

'''

def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("-------names-------")
for f in L:
    print(f)

print("-------call each of them-------")
for f in L:
    print(f(-2))

print("-------just the first one in the list-------")
print(L[0])
print(L[0](3))