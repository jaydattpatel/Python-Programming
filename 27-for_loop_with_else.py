'''
author : Jaydatt
Loops : for with else 
The else statement is one such statement that can be used in loops even
without the if conditional statement. 
Else is only functional when the loop is terminated normally. If the loop is terminated forcefully, the else statement is overlooked and not executed. 
'''

print('---------------1----------------')
for char in 'Hello!':  
    print ('char: ', char) 
else:
    print ('All letters were printed.') 

print('---------------2----------------')
for char in 'Hello!':  
    if(char == 'l'):
        break
    print ('char: ', char)
else:
    print ('All letters were printed.') 