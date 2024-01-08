'''
author : Jaydatt
range function
'''
print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print("(list(range(5))) : ", list(range(5)))
print("(list(range(0,5))) ", list(range(0,5)))

# Note: `range` function is already casted as `list` in the textbook
print("range(5): ",range(5))
