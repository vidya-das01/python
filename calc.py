def add(num1,num2):
	return num1+num2
def sub(num1,num2):
	return num1-num2
def multi(num1,num2):
	return num1*num2
def div(num1,num2):
	return num1/num2
def power(num1,num2):
	return num1**num2
def calc(num1,num2,operator):	
	if operator==1:
		print(add(num1,num2))
	elif operator==2:
		print(sub(num1,num2))
	elif operator==3:
		print(multi(num1,num2))
	elif operator==4:
		print(div(num1,num2))
	elif operator==5:
		print(power(num1,num2))
	else:
		print("invalid choice")
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print("1.addition \n2.subtraction \n3.multiplication \n4.division \n5.power")
operator=int(input("select the operator: "))
calc(num1,num2,operator)		

		

