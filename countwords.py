f = open("file.txt", "r")
c = 0

for x in f:
    words = x.split()  
    c += len(words)

print("The number of words:", c)

f.close()  
