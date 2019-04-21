
try:
    n =int(input())
    l = list(map(int,input().split()))
    
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            s = l[i] + l[j]
            # print(s)
            try:
                    
                if l.count(s) and l.index(s,j+1,n):
                    print(l[i],l[j],s)
            except:
                pass
except:
    print("Invalid Input")
                    
