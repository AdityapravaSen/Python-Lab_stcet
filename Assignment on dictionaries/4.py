d = {}
n = int(input("Enter the number of elements"))
for i in range(1, n+1):
    x = input("Enter the key")
    y = int(input("Enter the value"))
    d[x] = y
result = 1
for key in d:
    result = result * d[key]

print(result)
