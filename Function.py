def add(n1,n2):
    sum=n1+n2
    print(sum)
n1=input("Enter n1 value:")
n2=input("Enter n2 value:")
add(n1,n2)

age=int(input("Enter your age:"))
gen=input("enter gender:") 
def allowed():
   print("You ur allowed")
def restricted():
    print("you are restricted")
if(age>18 and gen=="male"):
    allowed()
else:
    restricted()

gen=input("enter gender:") 
def allowed():
    print("You ur allowed")
def restricted():
    print("you are restricted")
if(gen=="male"):
    allowed()
else:
    restricted()

#pass()
def add(a,b=None):
    if (b):
        print(a+b)
    else:
        print(a+a)
add(5)
add(5,6)