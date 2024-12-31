prompt="Enter the string: "
s=input(prompt)
res=""
for i in s:
    if i.islower():
        i=i.upper()
        res+=i
    elif i.isupper():
        i=i.lower()
        res+=i
    else:
        res+=i
print(res)

# Eg: HackerRank.com presents "Pythonist 2".