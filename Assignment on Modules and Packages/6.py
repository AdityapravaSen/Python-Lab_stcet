import F1
s = 0
i = int(input("Enter 1 for first function, 2 for second function, 3 for third function, 4 for fourth question and 5 for fifth function"))
if(i == 1):
    a = int(input("Enter the value of x"))
    b = int(input("Enter the value of y"))
    s = s+F1.f1(a, b)
    print("Answer is ", s)
elif(i == 2):
    n = int(input("Enter the value of n"))
    r = int(input("Enter the value of r"))
    s = s+F1.f2(n, r)
    print("Ans is ", s)
elif(i == 3):
    n = int(input("Enter the value of n"))
    s = s+F1.f3(n)
    print("Ans is", s)
elif(i == 4):
    m = int(input("Enter the value of m"))
    n = int(input("Enter the value of n"))
    s = s+F1.f4(m, n)
    print("Ans is", s)
elif(i == 5):
    m = int(input("Enter the value of m"))
    x = int(input("Enter the value of x"))
    s = s+F1.f5(m, x)
    print("Ans is", s)
else:
    print("Wrong input")
