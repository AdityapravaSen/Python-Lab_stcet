f = open("demo.txt")
c = 0
d = f.read()
l = d.split("\n")
for i in l:
    if i:
        c = c+1
print(c)
