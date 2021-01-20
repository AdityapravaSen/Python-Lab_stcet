a = open("K.txt", 'w')
b = open("hi.txt", 'r')
c = open("R.txt", 'r')
d = b.read()
e = c.read()
for i in d:
    a.write(i)
for i in e:
    a.write(i)
a.close()
b.close()
c.close()
