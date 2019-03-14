t = int(input())

l = list(map(int,input().split()))

for i in range(t):
    if i%2==0 and l[i]%2!=0:
        print(l[i],end =" ")
    elif i%2!=0 and l[i]%2==0:
        print(l[i], end = " ")
        
