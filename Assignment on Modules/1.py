s = int(input("Enter the start year"))
e = int(input("Enter the end year"))
print("The leap years are:")

for i in range(s, e):
    if((i % 4 == 0 and i % 100 != 0 or i % 400 == 0)):
        print(i)
