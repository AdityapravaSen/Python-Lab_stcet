st = input("enter the string")

digit = 0

vowel = 0

consonant = 0

special = 0

for i in range(0, len(st)):

    ch = st[i]

    if(ch >= 'a' and ch <= 'z')or(ch >= 'A' and ch <= 'Z'):

        ch = ch.lower()

        if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):

            vowel = vowel+1

        else:

            consonant = consonant+1

    elif(ch >= '0' and ch <= '9'):

        digit = digit+1

    else:

        special = special+1

print("string:", st)

print("vowel:", vowel)

print("consonant:", consonant)

print("digit:", digit)

print("special character:", special)
