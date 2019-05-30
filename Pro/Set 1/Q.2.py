try:
    n,k = map(int,input().split())
    lt = []
    for i in str(n):
        lt.append(i)

    if k > 0:
        lt = lt[k:]
        
        for i in lt:
            print(i,end = "")
    else:
        print(n)

except:
    print("Invalid Input")
