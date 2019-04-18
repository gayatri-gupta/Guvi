try:
    import math 
    l = list(map(int,input().split()))
    n = l[0]
    m = l[1]
    a = n*m
    b = math.sqrt(a)
    if b- math.floor(b)==0:
        print("yes")
    else:
        print("no")
except ValueError:
    print("Invalid Input")
