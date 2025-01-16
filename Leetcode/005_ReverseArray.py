l=[10,20,30,40,50]
# newl=l[-1::-1]
# print(newl)

# for i in range(len(l)-1,-1,-1):
#     print(l[i])

left=0
right=len(l)-1
while(left < right):
    temp=l[left]
    l[left]=l[right]
    l[right]=temp
    left=left+1
    right=right-1
print(l)