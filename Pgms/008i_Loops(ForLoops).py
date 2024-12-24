# range(5)
# start=0
# condition<5
# increment=1

# range(1, 6)
# start=1
# condition<6
# increment=1

# range(1, 6, 2)
# start=1
# condition<6
# increment=2

print("start=0 condition<5 increment=1")
for n in range(5):
    print("n=",n)
print()

print("start=1 condition<6 increment=1")
for i in range(1,6):
    print("i=",i)
print()

print("start=1 condition<6 increment=2")
for s in range(1,6,2):
    print("s=",s)
print()


# For reverse we always use all three variables
# range(10,0,-1)
# start=10
# stop=0
# decrement -1
print("start=10 stop=0 decrement=-1")
for p in range(5,0,-1):
    print("p=",p)