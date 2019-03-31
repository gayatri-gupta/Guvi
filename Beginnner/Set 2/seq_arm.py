l = list(map(int,input().split()))
n = l[0]
m = l[1]

for i in range(n,m+1):
    odr = len(str(i))  
    s=0
    t = i
    while t >0 :
        d = t%10
        s+= d**odr
        t = t//10
        
    if i ==s:
        print(i,end = " ")
