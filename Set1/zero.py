n = int(input())
l = list(map(int,input().split()))

for i in range(n-1):
    
    for j in range(i+1,n):
        
        if(l[i]+l[j]==0):
                
            print(l[i],l[j])
