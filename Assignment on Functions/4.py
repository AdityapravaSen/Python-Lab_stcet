def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def expo(a, b):
    return a**b


while True:
    num1 = int(input("enter 1st no.:"))
    num2 = int(input("enter 2nd no.:"))

    print("1.add\t2.substract\t3.multiply\n4.divide\t5.exponent\t6.exit")
    p = int(input("enter choice:"))

    if(p == 1):
        print("sum is: ", add(num1, num2))
    elif(p == 2):
        print("diff is: ", sub(num1, num2))
    elif(p == 3):
        print("prodict is: ", mul(num1, num2))
    elif(p == 4):
        print("quotient is: ", div(num1, num2))
    elif(p == 5):
        print("ans is: ", expo(num1, num2))
    elif(p == 6):
        break
    else:
        print("wrong choice")
