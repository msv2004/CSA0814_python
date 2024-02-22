try:
	age = int(input("Enter your age:\n"))
	print("Your age is: " + Age)
except ValueError:
  print("You have entered non-integer!")
except TypeError:
  print("You are performing operation on an incorrect object type!")
except NameError:
  print("You are using a variable that doesn't exist!")
except:
  print("Something else went wrong!!!")
