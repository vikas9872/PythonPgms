l=[10,20,30,40,50]
temp=l[0]
for i in range(1,len(l)):
    l[i-1]=l[i]
l[len(l)-1]=temp
print(l)