# Dictionaries
dict={
    1: "Vikas",
    2: "Vikram",
    3: "Nitin",
    4: "Ankit"
}

# print the dictionary
print("Dictionary: ",dict)

# get single element
print("Value of key 1: ",dict[1])
print("Value of key 2 using get: ",dict.get(2))
# type
print("Type of the dict: ",type(dict))

# length
print("Length of the dict: ",len(dict))

# change the value
dict[4]="Vikranth"
print("Dictionary after change: ", dict)

# get values
print("Values of the dictionary: ",dict.values())

# get keys
print("Keys in the dictionary: ",dict.keys())

# get items
print("Items returns dictionary in the form of list: ",dict.items())

# add items: i update ii square bracket
# i. update
dict.update({5: "Varun"})
print("dictionary after update of 5: ",dict)
# ii. square bracket
dict[6]="Arjun"
print("dictionary afrer adding 6: ",dict)

# delete items: 
dict.pop(6)
print("dictionary afrer removing 6: ",dict)
dict.clear()
print("After clearing the whole dictionary: ",dict)

# nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# nested dictionary second type
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)