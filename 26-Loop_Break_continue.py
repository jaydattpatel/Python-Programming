print("for loop break :-------")
for i in range(10):
    print(i)
    if i > 3:
        break
    print(i+100)
    
print("for loop continue :-------")
for i in range(10):
    print(i)
    if i > 3:
        continue
    print(i+100)

print("while break :-------")
i = 0
while (i<10):
    print(i)
    if i > 3:
        break
    print(i+100)
    i+=1
    
print("while continue :-------")
i = 0
while (i<10):
    if i > 3:
        i+=1
        continue
    print(i)
    i+=1
    