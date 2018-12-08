def ind_check(n,a):
    res = []
    for i in range(n):
        if i == a[i]:
            res.append(i)
    return res 

n = int(input("Enter Limit: "))
a = list(map(int, input().split()))
r = ind_check(n,a)
if r == []:
    print("-1")
else:
    for _ in r:
        print(_,end=" ")

