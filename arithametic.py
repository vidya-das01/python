num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation +, -, *, /, **, //, % ")

if(operator == "+"):
	 result = num1 + num2
elif(operator == "-"):
	result = num1 - num2
elif(operator == "*"):
	result = num1 * num2
elif(operator == "/"):
	result = num1 / num2	
elif(operator == "**"):
	result = num1 ** num2
elif(operator == "//"):
	result = num1 // num2
elif(operator == "%"):
	result = num1 % num2
else:
	print("invalid input")
	
print("the result is ",result)
