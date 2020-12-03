d = {}
n = int(input("Enter the number of elements"))
for i in range(1, n+1):
    x = str(input("Enter color:"))
    y = str(input("Enter number"))
    d[x] = y
for key in sorted(d):
    print("%s:%s" % (key, d[key]))
