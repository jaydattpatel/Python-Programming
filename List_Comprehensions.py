'''
author : Jaydatt Patel

List Comprehensions :
Python provides an alternative way to do map and filter operations, called a list comprehension. Many programmers find them easier to understand and write. List comprehensions are concise ways to create lists from other lists. The general syntax is:
    [<return_expression> for <item> in <list>]
    [<return_expression> for <item> in <list> if <expression>]

'''

print("-------------------- (1)")
things = [2, 5, 9]
yourlist = [value * 2 for value in things]
print(yourlist)

print("-------------------- (2)")
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list
print(keep_evens([3, 4, 6, 7, 0, 1]))


print("-------------------- (3)")
things = [3, 4, 6, 7, 0, 1]
print([x*2 for x in things if x % 2 == 0])
print("filter & map : ", map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

print("-------------------- (4)")
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [name[1] for name in people]

print("-------------------- (5)")
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [x*2 for x in lst]

print("-------------------- (6)")
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [s[0] for s in students if s[1]>=70 ]

print("-------------------- (7)")
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, 
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, 
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, 
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri = [dic['name'] for dic in tester['info']]
print(compri)


