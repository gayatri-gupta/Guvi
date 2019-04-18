n = int(input())
l = list(map(int, input().split()))
f = l[0]
r = l[1]
if f<n<r:
    print("yes")
else:
    print("no")
