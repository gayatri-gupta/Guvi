try:
    n = int(input())
    if n>13:
        if n%13==0:
            print("yes")
        else:
            print("no")
except ValueError:
    print("Invalid Input")
    
