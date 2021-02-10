def histogram(i):
    for n in i:
        j = ''
        k = n
        while(k > 0):
            j += '#'
            k = k - 1
        print(j)


histogram([3, 5, 7, 9])
