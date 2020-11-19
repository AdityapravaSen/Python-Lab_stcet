n = int(input("Enter number of rows of table : "))
n2 = int(input("Enter number of columns : "))
table = []
for i in range(1, n+1):
    a = []
    for j in range(1, n2+1):
        print("Enter element of", i, "row", j, "column : ", end="")
        k = int(input())
        a.append(k)
    table.append(a)
print(table)
