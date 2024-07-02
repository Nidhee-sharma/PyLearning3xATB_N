#Abstraction
#Encapsulation ,inheritance ,polymorphism
#class
#object
#constructor
#self, super ,__init__
#public ,_ ,__private

#Abstration
#Abstraction -oops
#hiding the details and showing the what is required
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        self.name =name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"

class Cat(Animal):

    def sound(self):
        return "Meow"

dog =Dog("rancho")
print(dog.sound())

cat = Cat("CAT")
print(cat.sound())