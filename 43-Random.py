''' 
author : Jaydatt
random function

(variable) def randrange(
    start: int,
    stop: int | None = None,
    step: int = 1
) (1): int = 1
) -> int
Choose a random item from range(stop) or range(start, stop[, step]).

Roughly equivalent to choice(range(start, stop, step)) but supports arbitrarily large ranges and is optimized for common cases.
'''
import random

print('--------------(1)--------------')
ran = random.random()  # random value range from 0.0 to 1.0 
print('num : ',ran)

print('--------------(2)--------------')
ran = random.randrange(1,7) # random value selected range(1 to 6)
print('num : ',ran)

print('--------------(3)--------------')
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rand_letter = random.choice(letters)
print('rand_letter : ',rand_letter)

print('--------------(4)--------------')
tuple = [('A',1),('B',2),('C',3)]
rand_tup = random.choice(tuple)
print('rand_tup : ',rand_tup)
