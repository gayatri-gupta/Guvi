x = list(map(int,input().split()))
n = x[0]
m = x[1]
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = (set(b)).issubset(set(a))
if(c):
    print("YES")
else:
    print("NO")
