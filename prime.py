n=int(input("enter the value: "))
isprime=1
for x in range(2,n):
    if(n%x==0):
        isprime=0;
if(isprime):
    print(n,"is a prime")
else:
    print(n,"not a prime")
    
