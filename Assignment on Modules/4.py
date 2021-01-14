import random

dice = [0 for i in range(6)]

for i in range(6000):
    x = random.randint(1, 6)
    dice[x-1] += 1

print("Frequency of occurance of each digit:")

for i in range(6):
    m = (dice[i]/6000)*100
    print(i+1, ":", m, "%")
