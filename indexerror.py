try:
	students = ["1. Nagesh","2. Mahesh","3. Ganesh"]
	index = int(input("Enter serial number of student: "))
	print("\n" + students[index-1])
except IndexError as error:
	print("\n" + error)
