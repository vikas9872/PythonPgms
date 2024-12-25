str="     Global academy of technology     "
# Capitalize: Capitalizes first letter in the sentence
caps=str.capitalize()
print("Capitalized string: ",caps)

# Uppercase
uppercase=str.upper()
print("Upper case String: ",uppercase)

# Lowercase
lowercase=str.lower()
print("Lower case String: ",lowercase)

# Title: Capitalizes first letter of each word
titlecase=str.title()
print("Titile String: ",titlecase)

# Strip: remove starting and ending white spaces
stripcase=str.strip()
print("Without space: ",stripcase)

# replace
replacestring=str.replace("y", "v")
print("Replaced y with v: ",replacestring)

# find: returns index of found string
findstr=str.find("y")
lastocc=str.rfind("y")
print("First occurance of y: ",findstr)
print("First occurance of y: ",lastocc)

# index
indexofy=str.index("y")
print("First occurance index of y: ",indexofy)
rindexofy=str.rindex("y")
print("Last occurance index of y: ",rindexofy)

# alpha: returns True if all characters in the string are in the alphabet
str1="Vikas"
alpha=str1.isalpha()
print("All letters of string are alphabets: ",alpha)

# chr: returns character of that ascii int value
print("Letter of the ascii 65: ",chr(65))

# ord: returns int of that ascii character
print("Value of A: ",ord("A"))

# For more: https://www.w3schools.com/python/python_strings_methods.asp