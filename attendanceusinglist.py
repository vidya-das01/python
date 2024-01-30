students=[]
n=int(input("enter the number of students: "))
days=int(input("enter the total number of days: "))
for i in range(n):
	name=input("enter the name of student: ")
	attendance=int(input("enter the number of present days: "))
	per=(attendance/days)*100
	students.append((per,name))
students.sort(reverse=True)
print(students)


