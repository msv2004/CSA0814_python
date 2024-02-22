num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if (num1 >= num2):
    if (num1 >= num3):
        result = num1

elif(num2 >= num3):
        result = num2
else:
        result = num3

print("The greatest of the three integers is:", result)
