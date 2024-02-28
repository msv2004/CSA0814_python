m = input("Enter a number: ")
result = len(m)
s = 0

for i in m:
    h = int(i) ** result
    s = s + h

    
if (s==int(m)):
    print("It is a armstrong number")
    
else:
    print("It is not a armstrong number")
