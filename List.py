
'''
author : Jaydatt
list [ , ]
list is mutable. tuple is immutable.
A list is a sequential collection of Python data values, where each value is identified by an index. The values that make up a list are called its elements. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.

There are several ways to create a new list. The simplest is to enclose the elements in square brackets ( [ and ]).
'''

## Creat list of fruits...............
myFruitList = ['Apple', 'Mango', 'Banana', 'Watermellan']
print('myFruitList: ',myFruitList)

print('(myFruitList * 3 ) : ',myFruitList * 3)
print('(myFruitList[0] * 3 ) : ',myFruitList[0] * 3)

### Fix Enter Input in integer and float............
myList = [11, 12, 41.5, 52.4]
myList.sort()
print('myList: ',myList)
print('max(myList): ', max(myList))
print('min(myList): ', min(myList))


newList = myList[:] # copy list new variable with new memory
print('newlist: ',newList)

newList1 = myFruitList[0:2] + myList[0:2]
print('newlist1: ',newList1)

friends = ["Amit", "Tom", "Rohan", "Sam", "Divya", 45]

# count the numbers of elements
print('len(friends) : ',len(friends))

print('friends: ', friends)

print('friends[0:3] : ', friends[0:3])
print('friends[-3:] : ', friends[-3:])

friends[-1] = [] # make empty last element
friends[0] = "Sagar" # replace element
friends[2:4] = ["Mayur","Jimit"]
print('friends: ', friends)


# compare two list
a = [81,82,83]
b = [81,82,83]

print("a : ",a)
print("b : ",b)
print("(a is b) : ",(a is b))
print("(a == b) : ",(a == b))

print("id(a) : ",id(a))
print("id(b) : ",id(b))

b = a
b[0] = 5
print("After b=a and b[0]=5,\na : ",a)

# List with tuples
scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))


# sum, reverse, sort, sorted, append(add), insert, del, remove, pop data in list.................
L1 = [5,3,7,1,9,4,8,2,6]
print('L1: \t',L1)

sumofL1 = sum(L1)        # sumofL1 = L1[0] + L1[1] + L1[2] + L1[3] + L1[4] + L1[5] + L1[6] + L1[7] + L1[8]
print('sum of L1 is',sumofL1)

L1.reverse()        # reverse L1 list
print('reverse:',L1)

L1.sort()           # sort elements in current list
print('sort:\t',L1)

LL = sorted(L1)     # sort elements and return new list 
print('sorted:\t',LL)

LL = sorted(L1, reverse= True)     # sort elements in reverse and return new list 
print('sorted reverse:\t',LL)

L1.append(10)     # add data in last in L1 list
print('append:\t',L1)

L1.insert(3,888)     # add data in specific position in L1 list
print('insert:\t', L1)

del L1[3]
print('del L1[3]:\t', L1)

del L1[3:5]
print('del L1[3:5]:\t', L1)

L1.remove(8)     # remove data in L1 list
print('remove 8:\t', L1)

L1.pop(3)   # pop() or pop(position) remove data from list
print('remove at pop(3):\t', L1)

print('L1.count(10) :\t',L1.count(10) ) # count specific data in list



l = ['w', '7', 0, 9]
m = l[1:2]
print('type(m) : ',type(m)) # list

l = ['w', '7', 0, 9]
n = l[1]
print('type(n) : ',type(n)) # string

# return mutable list
def circleInfo(r):
    cir = 2 * 3.14159 * r
    area = 3.14159 * r * r
    return [cir, area] # return mutable list

print(circleInfo(10))
circumference, area = circleInfo(10)
print("circumference : ",circumference)
print("area : ",area)


fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for item in enumerate(fruits):
    print(item[0], item[1])


