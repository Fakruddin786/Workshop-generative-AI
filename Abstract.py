#contract/blueprint
#from abc import ABC, abstractmethod

# Define an abstract class
#class Animal(ABC):
    
#    @abstractmethod
#    def sound(self):
#        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
#class Dog(Animal):
    
#    def sound(self):
#        return "Bark"  # Providing the implementation of the abstract method
#class Lion(Animal):
    
#    def sound(self):
#        return "ROAR"

# Create an instance of Dog
#dog = Dog()#Create object
#lion=Lion()#Create object
#print(dog.sound())# Output: Bark
#print(lion.sound())# Output:Roar

from abc import ABC, abstractmethod
class king(ABC):
    @abstractmethod
    def kingdom():
        pass
class Earl(king):
    def kingdom(self):
        return "Hail king loki"
    def mem1(self):
        return "decline king loki"
obj=Earl()
print(obj.kingdom())
print(obj.mem1())