'''
authour : Jaydatt Patel
Inheritance python
'''
# creating base or super class
class Person:

    # defining variable
    class_type = 'Person'

    # creating constructor for person
    def __init__(self,name='None',age=0):
        self.name = name
        self.age = age

    # method overriding
    def __str__(self):
        return "Name: {}, Age: {}".format(self.name,self.age)
    
    # method overriding
    def fun(self):
        return print('Base')
    
# creating derived class from base or super class    
class Student(Person):

    # overriding variable
    class_type = 'Student'

    # creating constructor for student
    def __init__(self,name,age,course):
        # calling super class constructor
        Person.__init__(self,name,age) # here self is current object that pass to super class 
        self.course = course

    # method overriding
    def __str__(self):
        return  "Name: {}, Age: {}, Course: {}".format(self.name,self.age, self.course)
    
    # method overriding
    def fun(self):
        return print('Derived')
    
print('------------------')    
p = Person('Amit',18)
p.fun()
print(p.class_type,p)

print('------------------')    
st = Student('Rahul',20,'Computer Engineer')
st.fun()
print(st.class_type,st)



