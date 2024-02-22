try:
	age = int(input("Enter your age:\n"))
	print("Your age is: ", age)
except ValueError:
  print("You have entered non-integer!")
except:
  print("Something else went wrong!!!")
