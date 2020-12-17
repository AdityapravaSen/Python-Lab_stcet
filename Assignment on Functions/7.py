def simpleInterest(p, t, r):
    if(r == "s"):
        return (p*t*12)/100
    else:
        return (p*t*10)/100


p = int(input("enter interest:"))
t = int(input("enter time-period:"))
print("enter s for senior citize, o for others:")
r = input()

print("simple interest is: ", simpleInterest(p, t, r))
