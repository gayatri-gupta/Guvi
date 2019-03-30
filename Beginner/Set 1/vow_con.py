n = input()
c = ord(n)
#ascii value from A to z
if 172 > c > 41:
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
