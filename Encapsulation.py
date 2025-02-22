class Bank:
    def __init__(self,name):
        self.__name=name
    def getData(self):
        return self.__name
obj=Bank("Loki")
print(obj.getData())

