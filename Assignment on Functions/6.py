def subject(name, sub):
    print(name, " likes to read:")
    for i in range(0, len(sub)):
        print(sub[i])


name = input("enter name:")
n = int(input("enter the no. of subjects u like:"))
sub = []
for i in range(0, n):
    sub_name = input("enter subject:")
    sub.append(sub_name)

subject(name, sub)
