#Inheritance
#acquire the attributes and behaviour
#Data members and methods

#father 3 bhk -house - Inheritance -son
#concept in object oriented programming (oop)
#that allows a class (child class) to inherit attributes and methods from another class (parent)

#Type of inheritance
# Single -80%
#multiple
#Multilevel
#hybrid
#hierarchical

#single example
class Grandparent:  #parent class , base class
    key = "abc@123"
    def grandparent_method(self):
        return "parent's method"

class father(Grandparent): #child class ,sub class
    def parent_method(self):
        return "parents method"

grandparent =Grandparent()
print(grandparent.grandparent_method())
print(grandparent.key)


parent =father()
print(parent.parent_method())
print(parent.grandparent_method()) #how parent is able to call the grandparent ?inheritance
print(parent.key)