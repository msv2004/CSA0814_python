def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)

num = int(input("Enter a Number:"))

if num<0:
    print("Enter Positive Number")
else:
    print("Sum is", sum(num))
