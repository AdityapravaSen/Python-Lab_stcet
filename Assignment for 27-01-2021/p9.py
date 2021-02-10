even = set()
composite = set()

k = 0
for i in range(1, 11):
    if(i % 2 == 0):
        even.add(i)

for i in range(2, 21):
    n = i
    k = 0even = set()
composite = set()

k = 0
for i in range(1, 11):
    if(i % 2 == 0):
        even.add(i)

for i in range(2, 21):
    n = i
    k = 0
    for j in range(1, n+1):
        if(n % j == 0):
            k = k+1
    if(k != 2):
        composite.add(n)

print("all() function:-")
print("even set:- ", all(even), "\n", "composite set:- ", all(composite), "\n")

print("len() function:-")
print("length of even set:- ", len(even))
print("length of composite set:- ", len(composite), "\n")

print("issuperset() function:-")

if composite.issuperset(even):
    print("composite is superset of even set")
else:
    print("composite is not a superset of even set")

print("\n")

print("sum() function:-")
print("even set sum is: ", sum(even))
print("composite set sum is: ", sum(composite))

   for j in range(1, n+1):
        if(n % j == 0):
            k = k+1
    if(k != 2):
        composite.add(n)

print("all() function:-")
print("even set:- ", all(even), "\n", "composite set:- ", all(composite), "\n")

print("len() function:-")
print("length of even set:- ", len(even))
print("length of composite set:- ", len(composite), "\n")

print("issuperset() function:-")

if composite.issuperset(even):
    print("composite is superset of even set")
else:
    print("composite is not a superset of even set")

print("\n")

print("sum() function:-")
print("even set sum is: ", sum(even))
print("composite set sum is: ", sum(composite))
