# python program to print initials of a name
def name(s):

    l = s.split()
    new = ""

    for i in range(len(l)-1):
        s = l[i]
        new += (s[0].upper()+'.')

    new += l[-1].title()

    return new


s = input("enter name:")
print(name(s))
