'''
Author : Jaydatt Patel
Decorators: In Python, decorators are a powerful feature that allows you to modify the behavior of a function or a method. They are a type of higher-order function, meaning they take a function as an argument and return a new function that can enhance or alter the behavior of the original function.
'''


# defining decorator and its wrapper function
def before_decorator(fun):
    def wrapper():
        fun()
        print("Before")
    return wrapper

def after_decorator(fun):
    def wrapper():
        fun()
        print("after")
    return wrapper

def log_decorator(fun):
    def wrapper():
        fun()
        print("log")
    return wrapper

# define main function using decorator
@before_decorator
@after_decorator
@log_decorator
def say_hello():
    print("Hello!")


# calling main function
say_hello()
