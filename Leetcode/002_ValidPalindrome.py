prompt="Enter the string: "
s=input(prompt)
news = ''.join(char.lower() for char in s if char.isalnum())
revs=news[::-1]
if news==revs:
    print("True")
else: 
    print("False")


# input: A man, a plan, a canal: Panama