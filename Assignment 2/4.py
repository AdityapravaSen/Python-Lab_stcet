ch = input("c for centigrade and f for fatenheit")

if(ch == "c"):
    temp = float(input("enter temp.:"))
    changed_temp = ((temp/5)*9)+32
    print("temp in farenheit is ", changed_temp)

elif(ch == "f"):
    temp = float(input("enter temp.:"))
    changed_temp = ((temp-32)*5)/9
    print("temp in celcius is ", changed_temp)
