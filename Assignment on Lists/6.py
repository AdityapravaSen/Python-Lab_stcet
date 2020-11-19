a=[]
b=[]
n=int(input("Enter the range of first list"))
for i in range(0,n):
    a.append(int(input("Enter the number")))
m=int(input("Enter the range of the second list"))
for i in range(0,m):
    b.append(int(input("Enter the number")))
list1=set(a)
list2=set(b)
if (list1==list2):
    print("The lists are equal")
else:
    print("The lists are not the same")