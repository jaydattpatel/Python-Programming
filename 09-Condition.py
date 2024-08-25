
'''
author : Jaydatt
In if-elif-else ladder elif and else are optional it is not mandatory.
syntax :
    if(expression):
        statements......
        ..........
    elif(expression):
        statements......
        ..........    
    else:
        statements......
        ..........    

Expression: boolean (<,>,<=,>=,==,!=,&,|,in,is,and,or)

'''
print('----------------------(1)')
aa = 15
bb = 15
print('id(aa) : ',id(aa))
print('id(bb) : ',id(bb))
print('(aa is bb) : ',(aa is bb))
print('(aa == bb) : ',(aa == bb))

print('----------------------(2)')
op = int(input('enter value of op(0,1,-1):'))
if(op==0):
    print("no")
elif(op>0):
    print("yes")
else:
    print("I am optional")

print('----------------------(3)')
## find given name is present or not in list
names = ["amit", "shubham", "rohit", "rohan", "aditi", "shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")


print('----------------------(4)')
# if else using "in"
l1 = [45, 56, 6]
d = int(input("enter any(45,56,6):"))
print(d in l1)
if (d in l1):
     print("yes")
else:
     print("no")

print('----------------------(5)')
## age compare sample
age = int(input("Enter your age: "))

if(age>18 and age<56):
    print("You can work with us")
else:
    print("You cannot work with us")

if(age>34 or age<50):
    print("ok")
else:
    print("not ok")
print('----------------------(6)')
## spam comment is defined as text containg keywords:"make a lot of money","buy now","click this","subscribe this"
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")


