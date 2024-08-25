'''
author : Jaydatt Patel
class in python

protected variable: The members of a class are not available to access from the exterior of the class. Accessibility is permitted within the class or its subclasses only. In Python, a data member is protected by prefixing it with a single underscore "_".
syntax: 
    _variableName
    _functionName()

private variable: Private members are secured, but these cannot be accessed even by the super or parent class's subclasses, and a double underscore "__" is used as a prefix to inform the interpreter that a data member is private. 
syntax:
    __variableName
    __functionName()
'''

class Fruit():
   def __init__(self, name, price):
      self.name = name
      self.price = price

   def sort_priority(self):
      return self.price

# creating list of Fruit objects 
L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]


print("---------sorted method-(1)-------")
for f in sorted(L, key=lambda x: x.price):
   print(f.name)

print("---------sorted method-(2)-------")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)


