x=10
def myFunc():
    x=5
    print("Value of x inside function: ",x)
myFunc()
print("Value of x outside function: ",x)
print()

y=100
def myNewFunc():
   # global y # global can be used to change the local to global variable
    y=200
    print("Value of y inside function: ",y)
myNewFunc()
print("Value of y outside function: ",y)