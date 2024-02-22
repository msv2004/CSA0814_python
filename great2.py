n1=float(input("Enter the value"))
n2=float(input("Enter the value"))

if n1 > n2:
    result = n1
elif n2 > n1:
    result = n2
else:
    result = "Equal"
print("The greatest number:",result)
