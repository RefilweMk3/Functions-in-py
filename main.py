name=input("Please enter ur name")
def intro(name):
    print("Hey" ,name)
intro(name)

def sub(a,b):
    print(a-b)

def add(a,b):
    print(a+b)

def div(a,b):
    print(a/b)

def multi(a,b):
    print(a*b)

a=int(input("Enter a number of ur choice "))
b=int(input("Enter another number "))
add(a,b)
sub(a,b)
div(a,b)
multi(a,b)