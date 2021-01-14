from datetime import datetime

now = datetime.now()

print("Year=", now.year)
print("Month=", now.month)
print("Day=", now.day)

current_time = now.strftime("%H:%M:%S")

print("Current Time =", current_time)
print(now)
