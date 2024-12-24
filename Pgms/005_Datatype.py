"""
    Mutable: Changes can be made
    Immutable: Changes cannot be made
"""
x=10
print(x, type(x))

z=1+10j
print(z, type(z))

y=1.0
print(y, type(y))

a="Vikas"
print(a, type(a))

l=[1, 2, 3, 4] # mutable
l[1]=100
print(l, type(l))

t=(1, 2, 3, 4) # Faster than list, There must be more than one item and are order list and also immutable
print(t, type(t))

d={
    1: "Alex", 
    2:"Braile", 
    3: "Chistopher"
} # Unordered collections in key value pairs and mutable
print(d, type(d))
# To get value
print(d[1])

s={1, 2, 3, 4, 5 ,6} # unordered collection of items and are immutable
print(s, type(s))