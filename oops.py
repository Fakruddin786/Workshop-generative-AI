#class Bike:
#    color="blue"
#    def __init__(self,name):
#        self.name=name
#    def bikeStarted(self):
#        print("bike started")
#    def bikeStoped(self):
#        print("bike stoped")
#b1=Bike("loki")
#b1.bikeStarted()
#b1.bikeStoped()
#print(b1.color)
#print(b1.name)

#class Car:
#    color="blue"
#    no_seats=5
#    def __init__(self,name):
#        self.name=name
#    def startAc(self):
#        print("car ac started")
#    def startSteroSpeakers(self):
#        print("car speaker started")
#b1=Car("loki")
#b1.startAc()
#b1.startSteroSpeakers()
#print(b1.color)
#print(b1.name)
#print(b1.no_seats)

class Car:
    color="green"
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Good Morning")
class Car1:
    color="yellow"
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("Godd morning from Car1")
c1=Car("THAR")
c2=Car1("MERCIDIES")
c1.greet()
print(c1.name)
print(c1.color)
c2.greet()
print(c2.name)
print(c2.color)