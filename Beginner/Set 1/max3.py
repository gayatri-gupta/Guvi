l = list(map(int, input().split()))
a = l[0]
b = l[1]
c = l[2]
if a>b : 
    if a>c:
        print(a)
elif b>a:
    if b>c:
        print(b)
else:
    print(c)
