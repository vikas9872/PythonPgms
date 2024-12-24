a=20
b=10

print("Arithmetic Operator")
print("Sum: ",a+b)
print("Difference: ",a-b)
print("Product: ",a*b)
print("Quotient: ",a/b)
print("Floor Quotient: ",a//b)  # // -- Floor Division
print("Remainder: ",a%b)
print("Exponent: ",a**2)
print()

print("Assigment Operator")
print(a)
a+=5 # a=a+5
print(a)
b-=2 # b=b-2
print(b)

print("Comparison Operatotr")
x=10
y=10
z=20
print("Is x=10 is == y=10? ",x==y)
print("Is x=10 is != y=10? ",x!=y)
print("Is x=10 is > z=20? ",x>z)
print("Is x=10 is < z=20? ",x<z)
print("Is x=10 is <= z=20? ",x<=z)
print("Is x=10 is >= y=10? ",x>=y)
print()

print("Logical Operators")
print("Is x<100 AND z<100? ",x<100 and z<100) # Both the statements true
print("Is x < 100 OR y>10? ", x<100 or y>10) # One of the statements is true
print("NOT(Is x<100 AND z<100?) ",not(x<100 and z<100)) # Opposite the real result
print()

print("Membership Operators")
s="Hello"
print("Is e in s? ","e" in s) # in -- To check whether character or string is present in the main string
print("Is a in s? ","a" in s)
print("Is e not in s? ","e" not in s) # not in -- To check whether character or string is not present in the main string
print("Is a not in s? ","a" not in s)
print()

print("Identify Operators")
print("Is s is Hello? ",s is "Hello") # returns true if both the variables are same
print("Is s is not Vikas? ",s is not "Vikas" ) # returns true if both the variables are not same
print()

print("Bitwise Operators")
u=10
v=8
print(bin(u))
print(bin(v))
print("Bits of u and v",bin(u&v))
print("Bits of u or v",bin(u|v))
print("Bits of u xor v",bin(u^v))