try:
	age = int(input("Enter your age: "))
	
	if (age > 100):
		raise Exception("Unacceptable Age Exception !")
		
	print("\n" + "Your age is: ", age)
except Exception as error:
	print("\n" + str(error))
