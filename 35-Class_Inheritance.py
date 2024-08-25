'''
authour : Jaydatt Patel
Inheritance python
protected variable: The members of a class are not available to access from the exterior of the class. Accessibility is permitted within the class or its subclasses only. In Python, a data member is protected by prefixing it with a single underscore "_".
syntax: 
    _variableName
    _functionName()

private variable: Private members are secured, but these cannot be accessed even by the super or parent class's subclasses, and a double underscore "__" is used as a prefix to inform the interpreter that a data member is private. 
syntax:
    __variableName
    __functionName()
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



