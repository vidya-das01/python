num=int(input("enter the number: "))
names=[]
for i in range(num):
	names.append(input("enter the name: "))
names.sort()
for i in names:
	print(i)	
