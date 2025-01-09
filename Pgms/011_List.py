"""
    List:
    # Mutable
    # Declared in []
    # comma seperated
"""

l=[10, 20, 30, 40, 50, "Hello"]
# Check the type
print("Type of list: ",type(l))

# Reverse list
newl=l[-1::-1]
print("Reversed list: ",newl)

# Get usig list element
print("Element at index 3: ",l[3])

# Get multiple list elements
print("Element at index 1, 2, 3, and 5: ",l[1],l[2],l[3],l[5])

# Slicing the list
print("Slicing list from 2 to 4: ",l[2:5])

# Increment in list
print("List after 2 increment: ",l[0::2])

# list as constructor
l1=(l)
print("List created using list constructor: ",l1)