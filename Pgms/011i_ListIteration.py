l=[1,20,3,40,5,60]
# Using length
print("Using length of the string: ")
for i in range (len(l)):
    print(l[i])
print()

# Without using length
print("Without using length of the string: ")
for a in l:
    print(a)
print()

# Even numbers in the lists
print("Even numbers in the list: ")
for i in range (len(l)):
    if l[i]%2==0:
        print(l[i])
print()

# Reversing the list:
print("Reverse the list: ")
for n in range (len(l)-1,-1,-1): # parameters: length-1, -1(Goes till 0), -1(Iteration)
    print(l[n])