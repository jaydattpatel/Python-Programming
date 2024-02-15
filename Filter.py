'''
author : Jaydatt Patel
filter function : 
filter takes two arguments, a function and a sequence. The function takes one item and return True if the item should. It is automatically called for each item in the sequence.
'''
print("-------------------- (1)")
nums = [3, 4, 6, 7, 0, 1]
evens = list(filter(lambda num: num % 2 == 0, nums))
print(evens)

print("-------------------- (2)")
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing = list(filter(lambda word : 'w' in word, lst_check))
print(filter_testing)

print("-------------------- (3)")
things = [3, 4, 6, 7, 0, 1]
# usin map and filter 
print("filter & map : ", list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))))


