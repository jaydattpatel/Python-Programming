
'''
author : Jaydatt
sorted() Function Syntax: sorted(iterable, key, reverse)

Parameters: sorted takes three parameters from which two are optional. 

Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.

Key(optional): A function that would serve as a key or a basis of sort comparison.

Reverse(optional): If True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.

Return: Returns a list with elements in sorted order.

'''

print("----------Sorted List--------")
L1 = [5,3,-7,1,9,4,-8,2,6]
LL = sorted(L1)    # sort elements and return new list 
print('sorted:',LL)
LL = sorted(L1, reverse= True)# sort elements in reverse and return new list 
print('sorted reverse:',LL)


print("----------Sorted List by function absolute------")
def absolute(x):
    if (x>=0): 
        return x 
    else: 
        return -x
    
LL = sorted(L1, key = absolute)# sort elements in reverse and return new list 
print('sorted absolute:',LL)

LL = sorted(L1, reverse= True, key = absolute)# sort elements in reverse and return new list 
print('sorted reverse absolute:',LL) 


print("------------Sorted String Characters --------")
s1 = "Hello"
s2 = sorted(s1)    # sort elements and return new list 
print('sorted string:',s2)
s2 = sorted(s1, reverse= True)# sort elements in reverse and return new list 
print('sorted string reverse:',s2)


print("---------Sorted with Lambda Function by Last Digit------")
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

sorted_lambda = sorted(nums, key = lambda x : x[-1])
print('sorted_lamda:',sorted_lambda)

sorted_lambda = sorted(nums, reverse = True, key = lambda x : x[-1])
print('sorted_lamda reverse:',sorted_lambda)



print("---------Sorted with Lambda Function by dictionary key or values---")
L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']
dics = {}
for x in L:
    if x not in list(dics.keys()):
        dics[x] = 1
    else:
        dics[x] +=  1

print("dics : ",dics)

print("Sort by keys: ")
sorted_keys = sorted(dics)
for x in sorted_keys:
    print("K:{}, V:{} ".format(x, dics[x]))

print("Sort by values: ")
sorted_keys = sorted(dics, key = lambda x : dics[x])
for x in sorted_keys:
    print("K:{}, V:{} ".format(x, dics[x]))



print("-------Sorted Dictionary with List by lambda------")
states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}
# count how many city start from 's' in state of states
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

#sort dictionary keys by count how many city start from 's' in state of states
print(sorted(states, key=lambda state: s_cities_count(states[state])))



print("----------Sorted Tuples List ---------- : ")
# In Sorted Tuple List, Tuple sorted first by first elements, then second elements and so on and return finel list
tups = [('A', 3, 2),
        ('C', 1, 4),
        ('B', 3, 1),
        ('A', 2, 4),
        ('C', 1, 2)]
print("tups : ", tups)
sorted_tup =  sorted(tups)
print("sorted_tup : ",sorted_tup)


print("-----------Sorted List by Tuples---------- : ")
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
print("fruits : ", fruits)

# sort first by length of string then comparing string
sorted_fruits = sorted(fruits, 
                   key=lambda fruit_name: (len(fruit_name), fruit_name))
print("sorted_fruits : ", sorted_fruits)


print("-----------Sorted Dictionary by Tuples---------- : ")

weather = {'Reykjavik': {'temp': 60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

# sort first by city name and then sort by temp
sorted_weather = sorted(weather, 
                        key=lambda w: (w, weather[w]['temp']))
print("sorted_weather : ", sorted_weather)
