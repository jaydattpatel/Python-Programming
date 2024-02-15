'''
author : Jaydatt Patel
class in python
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


