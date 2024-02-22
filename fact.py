n = int(input("Enter a Number:"))

i = 1
fact = 1


while i <= n:
    fact = fact * i
    i+=1

print("Factorial of ",n,"!:",fact)
