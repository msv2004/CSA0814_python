n=int(input("E:\n"))
sum=0
for i in range(1,n):
  if n%i == 0:
    sum=sum+i
if sum==n:
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")
