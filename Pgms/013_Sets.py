"""
    sets:
    unordered, unindexed
"""
# create set
set1={1, 2, 3, 4, 5}
print("Set: ",set1)

# print element in set
for i in set1:
    print(i)

# add()
set1.add(100)
print("100 is added to the set: ",set1)

# update()
set2={10,20,30,40,50}
set1.update(set2)
print("set 1 after update with set2: ",set1)

# pop()
popElement=set2.pop()
print("Set2 after element after popped: ",set2)

# discard()
discardedElement=set1.discard(2)
print("Set 1 after discartion: ",set1)

# intersection
set3={100, 200, 300, 400, 500}
set4={200, 300, 100, 600, 700, 1000}
res2=set3.intersection(set4)
print("items in the both sets: ", res2)

# difference
res=set3.difference(set4)
print("difference(): items in set3 but not in set4: ",res)

# symmetric_difference
res1=set3.symmetric_difference(set4)
print("symmetric_difference(): all items except duplicates: ",res1)