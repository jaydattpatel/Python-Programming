'''
author : Jaydatt Patel
class in python
'''

class Point:
    # creating variables 
    var1 = 1234
    var2 = 'Python'    

    # constructor with default paramere arguments
    def __init__(self,x = 999,y = 999): # self is currunt pointing object, like 'this' in java or c++ 
        self.x = x    # if var not defined in self class then it will define new variable
        self.y = y

    # function in class
    def show(self):
        return {'X' : self.x,'Y' : self.y}

# creating an object using different constructor
obj1 = Point(25,41)    
obj2 = Point(9,13)      
obj3 = Point(50)  
obj4 = Point(y=15,x=16)
obj5 = Point()

print("obj1 is obj2 : ", obj1 is obj2)
print('------------1-------------')
print('obj1 :', obj1.show())
print('obj2 :', obj2.show())
print('obj3 :', obj3.show())
print('obj4 :', obj4.show())
print('obj5 :', obj5.show())
print('------------2-------------')
Point.get = 55  # create variable in class at anywere
obj1.z = 10     # create variable in only for object at anywere

print('Point.get : ',Point.get)

print('obj1.get : ',obj1.get)
print('obj1.z : ',obj1.z)

print('------------3-------------')
obj1.var1 = 356  # this willl
print("Point.var1 : ",Point.var1)
print("obj1.var1 : ",obj1.var1)
print("obj2.var1 : ",obj2.var1)

print('------------4-------------')
Point.var1 = 985
print("Point.var1 : ",Point.var1)
print("obj1.var1 : ",obj1.var1)
print("obj2.var1 : ",obj2.var1)
