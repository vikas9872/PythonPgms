"""
    Tuples:
    1. Immutable
    2. works in ()
    3. ordered datatype
"""

# create tuple
tup=(1, 2, 3, 4, 5)
print("Tuples: ",tup)

# type
print("Type: ",type(tup))

# accessing tuple items
print("Accessing item using indexing: ",tup[2]) # negetive indexing can also be used
print('Accessing tuples using loop: ')
for i in tup:
    print(i)

# slicing tuples
print("Slicing tuples between 1 to 4: ",tup[1:4])

# check if item present in tuple
for i in tup:
    if i == 2:
        print("Yes, 2 is present in the tuple")

# to add items to tuples: Convert tuple to list
l=list(tup)
l.append(20)
print("Item added to tuple after converting it to list: ",l)

# one tuple can be added to another
tup1=("Vikas",)
tup+=tup1
print("Two tuples can be added: ", tup)