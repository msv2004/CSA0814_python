a = [[2, 4, 6, 8], [1, 3, 5, 7]]
b = [[8, 6, 4, 2], [7, 5, 3, 1]]
c = [[0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        c[i][j] = a[i][j] + b[i][j]

for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end=" ")
    print()
