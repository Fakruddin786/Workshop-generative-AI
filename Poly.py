class Father:
    def status(self):
        print("This is my property")
class Son(Father):
    def status(self):
        print("This is my father")
obj1=Son()
print(obj1.status())