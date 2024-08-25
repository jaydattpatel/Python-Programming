'''
author : Jaydatt Patel

Zip :
The zip function takes multiple lists and turns them into a list of tuples (actually, an iterator, but they work like lists for most practical purposes), pairing up all the first items as one tuple, all the second items as a tuple, and so on. Then we can iterate through those tuples, and perform some operation on all the first items, all the second items, and so on.

'''
print("----------------------(1)")
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = list(zip(L1, L2))
print(L3)

L4 = []
for (x1, x2) in L3:
    L4.append(x1+x2)
print(L4)

print("----------------------(2)")
L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

print("----------------------(3)")
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x1+x2 for(x1,x2) in list(zip(L1,L2)) if x1>10 and x2<5]
print(L3)


print("----------------------(4)")
L3 = list(map(lambda x: x[0] + x[1], list(zip(L1, L2))))
print(L3)

print("----------------------(5)")
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda x : len(x[0])>3 and len(x[1])>3 ,list(zip(l1,l2))))
print(opposites)


print("----------------------(6)")
# Consider a function called possible, which determines whether a word is still possible to play in a game of hangman, given the guesses that have been made and the current state of the blanked word.
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))