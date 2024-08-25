'''
author : Jaydatt Patel
overide methods in class in python
'''

class Point:
   # constructor
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    # override function : __str__()  for class to string cast.
    def __str__(self):
       return 'Point(__str__) : x = {} , y = {}'.format(self.x,self.y)

    # override function : __add__() 
    def __add__(self,other):
       return Point((self.x + other.x) , (self.y + other.y)) # return new Point by adding two objects
    
    # override function : __str__() 
    def __sub__(self,other):
       return Point((self.x - other.x),(self.y - other.y)) # return new Point by subtracting two objects

obj = Point()
print('Override(__str__) : ',obj)

obj1 = Point(25,41)    # Instantiate an object
obj2 = Point(9,13)     # make a second 
obj3 = obj1 + obj2
print('add: ',obj3)
print('sub: ',obj1 - obj2)


