def find_gcd(x, y):
    while(y):
        x, y = y, x % y

    return x


arr = []
n = int(input("enter the limit:"))

for i in range(0, n):
    num = int(input("enter nos.:"))
    arr.append(num)

num1 = arr[0]
num2 = arr[1]
gcd = find_gcd(num1, num2)

for i in range(2, len(arr)):
    gcd = find_gcd(gcd, arr[i])

print(gcd)
