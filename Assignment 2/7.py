x = int(input("enter no:"))
y = int(input("enter no:"))
z = int(input("enter no:"))

if(x > y and x > z):
    print(x, " is max")
elif (y > x and y > z):
    print(y, " is max")
else:
    print(z, " is max")


if(x < y and x < z):
    print(x, " is min")
elif (y < x and y < z):
    print(y, " is min")
else:
    print(z, " is min")
