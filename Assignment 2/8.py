hrs = input("Enter no.of hrs worked: ")
rate = input("Enter the rate per hour: ")

try:
    hrs = int(hrs)
    rate = int(rate)
except:
    print('Non numeric data found.')
