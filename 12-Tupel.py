
'''
author : Jaydatt
tupel make list with ( , ) or only by seperating ',' without any bracks.
tuple is immutable. list is mutable.

A tuple, like a list, is a sequence of items of any type. The representation is just like lists, except with parentheses () instead of square brackets [].

The key difference between lists and tuples is that a tuple is immutable, meaning that its contents can’t be changed after the tuple is created.

below function not allowed in function if tupel list l1 :

    l1[0] = 3       -------not allowed to change data for tupel list
    l1.reverse()    -------not allowed to reverse data for tupel list
    l1.sort()       -------not allowed for tupel list
    l1.append()     -------not allowed for tupel list
    l1.inset()      -------not allowed for tupel list
    l1.remove()     -------not allowed for tupel list
    l1.pop()        -------not allowed for tupel list
'''

##To create a tuple with a single element (but you’re probably not likely to do that too often), we have to include the final comma, because without the final comma, Python treats the (5) below as an integer in parentheses:
t = (5,)  ## tuple
print(type(t))
x = (5)     ##integer
print(type(x))

tup = (1, 2, 5, 3, 6, 4, 7, 2 ,2)
print(tup)

# count the numbers of elements
print('len(tup): ', len(tup))

cnt = tup.count(2)     # count specific data used in list array
print('counts of 2 is :', cnt)

dex = tup.index(7)     # get index number of specific data of L1 list
print('index(7) :', dex)

sumofl1 = sum(tup)        # sumofL1 = L1[0] + L1[1] + L1[2] + L1[3] + L1[4] + L1[5] + L1[6] + L1[7] + L1[8]
print('sum of L1 is',sumofl1)

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
#print(add(z))# this line causes an error
print("add(*z) : ",add(*z)) # pass tuples to function argument


def getTuples():
    x = 11
    y = 21
    return x,y # or (x,y)

tp = getTuples()
print("tp : ",tp)


# pack Tupels
julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

# unpack Tupels
name, surname, birth_year, movie, movie_year, profession, birth_place = julia

# assign values to variables 
(a, b, c, d) = (1, 2, 3,4)

# swap the values 
(a, b) = (b, a)


# iterator with tuples
authors = [('Paul', 'Resnick'), ('Brad', 'Miller'), ('Lauren', 'Murphy')]

for first_name, last_name in authors:
    print("first :", first_name, ", last :", last_name)