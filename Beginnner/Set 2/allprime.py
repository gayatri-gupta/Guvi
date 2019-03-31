l = list(map(int,input().split()))

n = l[0]
m = l[1]

for i in range(n+1,m+1):
    if i >1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
