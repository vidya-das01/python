student={}
n=int(input("enter the number of students: "))
for i in range(n):
	name=input("enter the name: ")
	age=input("enter your age: ")
	grade=input("enter the grade: ")
	student[name]=age,grade
print(student)	
