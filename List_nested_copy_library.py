'''
author : Jaydatt

Nested List and access or copy

Deep copy with copy library for multi nested sub-list

'''

import copy

original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy = original[:]
deeply_copied = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied)
print("-------- shallow copy -----------")
print(shallow_copy)