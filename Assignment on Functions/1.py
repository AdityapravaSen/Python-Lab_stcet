def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def fibonacci(n):
    a = 0
    b = 1
    print(a, b, end=" ")
    while(n-2):
        c = a+b
        a = b
        b = c
        print(c, end=" ")
        n = n-1


nterms = int(input("Plese enter a positive integer:"))
print("Fibonacci sequence using recursion:")
for i in range(nterms):
    print(recur_fibo(i))

# print("\n")
print("Fibonacci sequence without recursion:")
fibonacci(nterms)
