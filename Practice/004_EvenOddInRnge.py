prompt="Enter the number: "
num=int(input(prompt))
for i in range(num):
    if i%2==0:
        print(i,"Even Number")
    else:
        print(i,"Odd Number")