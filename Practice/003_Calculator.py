prompt1="Enter the first number: "
num1=int(input(prompt1))
prompt2="Enter the second number: "
num2=int(input(prompt2))
prompt3="Enter the operator(+, -, *, /, //): "
operator=input(prompt3)
if operator=="+":
    print("Sum: ",num1+num2)
elif operator=="-":
    print("Difference: ",num1-num2)
elif operator=="*":
    print("Product: ",num1*num2)
elif operator=="//":
    print("Floor Quotient: ", num1//num2)
elif operator=="/":
    print("Quotient: ",num1/num2)
else: 
    print("Select any operator")