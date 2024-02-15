'''
author : Jaydatt

Nested List and access or copy

Deep and Shallow Copies:
cloning and aliasing lists we had mentioned that simply cloning a list using [:] would take care of any issues with having two lists unintentionally connected to each other. That was definitely true for making shallow copies (copying a list at the highest level), but as we get into nested data, and nested lists in particular, the rules become a bit more complicated. We can have second-level aliasing in these cases, which means we need to make deep copies.

When you copy a nested list, you do not also get copies of the internal lists. This means that if you perform a mutation operation on one of the original sublists, the copied version will also change. We can see this happen in the following nested list, which only has two levels.

'''

print("------------shallow copy - 1------------")
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied = original[:]
print("copied : ",copied)
print("copied is original : ",copied is original)
print("copied == original : ", copied == original)
original[0].append(["canines"])
print("original : ",original)
print("copied : ",copied)


print("------------deep copy - 1------------")
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied.append(copied_inner_list)
print("copied: ",copied)
print("copied is original : ",copied is original)
print("copied == original : ", copied == original)
original[0].append(["canines"])
print("original : ",original)
print("copied : ",copied)