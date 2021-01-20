f1 = open("hi.txt", "r")
f2 = open("new_file.txt", "w")
data = f1.read()
for c in data:
    if (c.isalpha() and c.islower()):
        f2.write(c.upper())
    elif (c.isalpha() and c.isupper()):
        f2.write(c.lower())
    else:
        f2.write(c)
f1.close()
f2.close()
f = open("new_file.txt", "r")
data = f.read()
print(data)
f2.close()
