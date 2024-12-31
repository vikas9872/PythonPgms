li=[1,2,3,4,5,6]
firstP=max(li)
secondP=0
for i in li:
    if i<firstP:
        secondP=i
print("Second max number: ",secondP)