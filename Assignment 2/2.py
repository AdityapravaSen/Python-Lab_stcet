rate = int(input("enter rate:"))
hours = int(input("enter hours:"))

regular = hours*rate
if(hours > 40):
    overtimeRate = 1.5*rate
    overtime = (hours-40)*overtimeRate
    totalpay = regular+overtime
    print("pay is ", totalpay)
else:
    print("pay is ", (rate*hours))
