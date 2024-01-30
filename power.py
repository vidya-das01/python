def power(base,expo):
	if expo==0:
		return 1
	if expo==1:
		return base
	else:
		return base*power(base,expo-1)
base=int(input("enter the first number"))
expo=int(input("enter the second number"))
print(power(base,expo))


