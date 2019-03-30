q = list(map(int,input().split()))
n = q[0]
k = q[1]
l = list(map(int, input().split()))

sum = 0
for i in range(k):
    sum+=l[i]
print(sum)

