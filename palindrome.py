def palin(n):
	rev=int(str(n)[::-1])
	if rev==n:
		return("palindrome")
	else:
		return("not palindrome")
num=int(input("enter a number: "))
result=palin(num)
print(result)		
