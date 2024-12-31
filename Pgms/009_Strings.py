print('A string inside single qupte')
print("A string inside double quote")
print('"Double quote" string inside the single quote string')
print("'Single quote' string inside double quote string")
print("String with \"escape\" sequence")


str="Global Academy of Technology"
print("Element at end of the string: ",str[-1])
# String slicing
print("Substring from 0 to 6-1=5: ",str[0:6]) # str[start: end]
print("String from 0 to end: ",str[0:])
print("String  just using \":\" without providing start and end: ",str[:])
# Increment string
print("String from 0 with increment 2: ",str[0::2]) # str[start:: increment]
# Reverse string
print("Reverse the string: ",str[::-1])
# Reversing the substring
print("Reversing the substring: ",str[-1:-11:-1]) # str[start: end: increment]
# substring using for loop
print("Substring from 4 to end with increment: ")
for j in range(10,len(str),1):
    print(str[j])
# count
count=0
for i in str:
    if i=="y":
        count+=1
print("Number of y: ",count)
# starts with
print("Does the str start with G: ",str.startswith("G"))