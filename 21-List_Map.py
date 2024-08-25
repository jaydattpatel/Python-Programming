'''
author : Jaydatt Patel
Map function : 
map takes two arguments, a function and a sequence. The function is the mapper that transforms items. It is automatically applied to each item in the sequence.
'''

print("-------------------- (1)")
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print("things3 : ",things3)

print("-------------------- (2)")

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things4 = quadrupleStuff(things)
print("things4 : ",things4)

print("-------------------- (3)")

things = [2, 5, 9]
things4 = map((lambda value: 4*value), things)
print(list(things4))

print("-------------------- (4)")

print(list(map((lambda value: 5*value), [1, 2, 3])))

print("-------------------- (5)")

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled = list(map(lambda x: x*2 , lst))
print("greeting_doubled : ",greeting_doubled)

print("-------------------- (6)")

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
abbrevs_upper = list(map(lambda x: x.upper(),abbrevs))
print("abbrevs : " ,abbrevs_upper)

print("-------------------- (7)")
things = [3, 4, 6, 7, 0, 1]
# usin map and filter 
print("filter & map : ", map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))