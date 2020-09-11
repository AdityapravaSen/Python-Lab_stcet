import math

a = int(input("enter coeff. of x^2:"))
b = int(input("enter coeff. of x:"))
c = int(input("enter coeff. of 1:"))

d = (b**2)-(4*a*c)

if d < 0:
    print("roots are imaginary")
else:
    r1 = ((-b) + math.sqrt(d))/2*a
    r2 = ((-b) - math.sqrt(d))/2*a
    print("root 1: ", r1, "\nroot 2: ", r2)
