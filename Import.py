''' 
author : Jaydatt

import file and function
syntax: 
1. import file_name
2. from file_name import function_name

create file named 'Import_mycode'
code{

def fun(x) :
    print(x)

def fun2(x) :
    print(x,x)
}

'''

from Import_mycode import fun
fun('Welcome to Python')

# or

import Import_mycode
Import_mycode.fun2('Welcome to Python')