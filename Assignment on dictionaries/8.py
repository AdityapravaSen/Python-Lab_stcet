old_dict = {}
n = int(input("Enter the number of elements"))
for i in range(1, n+1):
    x = str(input("Enter key:"))
    y = str(input("Enter number"))
    old_dict[x] = y
new_dict = dict([(value, key) for key, value in old_dict.items()])
print("Original dictionary is : ")
print(old_dict)
print()
print("Dictionary after swapping is :  ")
print("keys: values")
for i in new_dict:
    print(i, " :  ", new_dict[i])
