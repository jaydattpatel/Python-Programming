'''
author : Jaydatt

set: values in set will nor repeat and we can not change value in sets

'''

## values in set will nor repeat and we can not change value in sets
a = {1, 3, 4, 5, 1}
print('type of a is ',type(a))
print(a)

# Important: This syntax will create an empty dictionary and not an empty set
b = {}
print('type of b is ',type(b))

# An empty set can be created using the below syntax:
c = set()
print('type of c is ',type(c))


# copy whole set into another set
t1 = { 1,2,3}
t2 = {'a','b','c'}
t1.update(t2)
print('t1 : ', t1)

e = set() # Creating an empty set
## Adding values to an empty set
e.add(3)
e.add(4)
e.add(5)
e.add(5) # Adding a value repeatedly does not changes a set
e.add((5, 6, 7))
e.add(8) #addin tupels value     but # b.add({4:5}) Cannot add list or dictionary to sets
## Accessing Elements
print('after add data in e:', e)
## Length of the Set
len = len(e)
print('length of e:',len) # Prints the length of this set

## Removal of an Item

# Removes 5 from set e but 
e.remove(5) 
print("after remove '5':", e)
# Error :  e.remove(15)  #throws an error while trying to remove 15 (which is not present in the set)

## pop will remove random data in sets
print(e.pop())
print('after pop:',e)

## clear all data of set
e.clear()
print('after e.clear(), e :',e)


##
e = {11,12,13,14,15}
f = {14,15,16,17,18}
print('Union of e U f: ',e.union(f))
print('intersection of e A f: ',e.intersection(f))

print('Union of e U {1,2,11}: ',e.union({1,2,11}))

## creat set 18(int) and 18(string) and print 
s = {18, "18", 18.1}        ## in the set 18 is ineger & "18" is string so both are different
print('values in s:',s)

##   create set 20(int) 20.0(float) and 20(string) and print it with length
s2 = {20, 20.0, "20"}       ## in the set 20 is ineger and 20.0 is float which are same & "18" is string different
# so lenght will be 2
print('values in s2:', s2)
