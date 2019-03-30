n = input()

if len(n) > 1:
    print("No")
else:
    #ascii value from A to z
    c = ord(n)
    if 122 > c > 65:
        print("Alphabet")
        
    else:
        print("No")
