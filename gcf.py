def hcf(x,y):
    if x<y:
        lower=x
    else:
        lower=y
    while(True):
        if(lower%x==0 and lower%y==0):
            GCD==lower
            break
        lower-=1
    return GCD
m=int(input())
n=int(input())
result = hcf(m,n)
print(result)
