"""
    Functions to delete from list:
    1. del: works on index number Eg: del list_name[index_number]
    2. pop: normal pop function with index number Eg: list_name.pop(index_number)
    3. remove: removes the corresponding element Eg: list_name.remeove(element_that_has_to_be_removed)
    4. clear: clears complete list
"""
# l=[1, 2, 3, 4, 5, 9, 7, 6, 8]
# newl=[]

# DELETE FUNCTION
# del l[4] # element: 5 is deleted which is at index=4
# for i in l:
#     newl.append(i)
# print("List after deletion of element at index=4: ",newl)
# print()

# POP FUNCTION
# l.pop(5) #  element: 9 is deleted which is at index=5
# for a in l:
#     newl.append(a)
# print("List after the pop of element at index=5: ",newl)
# print()

# REMEOVE FUNCTION
# l.remove(5)
# for a in l:
#     newl.append(a)
# print("List after removing the element 5: ",newl)
# print()

# CLEAR FUNCTION
# l.clear()
# print(l)

# -------------------------------------------------------------------------------------------------------------------------
"""
    Update functions:
    1. insert: list_name[index_number,value_to_be_inserted]
    2. append: 
        i. adds element to the end of the list 
            list_name.append(element_to_be_appended)
        ii. add new list
            list_name1.append(list_name2)
    3. extend: merges new list with old list: list_name1.extend(list_name2)
"""


li=[10,20,3,40,5,7]
newli=[]
li2=[1, 6, 8, 9]

li.insert(1,100)
print("List after inserting 100 at index 1: ",li)


for i in li:
    if i%2!=0:
        newli.append(i)
print("New list with odd numbers: ",newli)

li.extend(li2)
print("After extending list1 with list2: ",li)