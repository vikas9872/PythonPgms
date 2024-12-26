# Normal formula
print("Normal formula: ")
l=[]
for i in range(1, 6):
    l.append(i)
print(l)

# List comprehension
print("List comprehension: ")
n=[m for m in range(1,6)]
print(n)

# With condition
print("List of even numbers: ")
n=[m for m in range(1,6) if m%2==0]
print(n)