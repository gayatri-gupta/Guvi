l = list(map(int,input().split()))

n = l[0]
m = l[1]

for i in range(n+1,m):
    if i%2!=0:
        print(i,end=" ")
