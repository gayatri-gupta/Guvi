def great(n,a):
    a.sort()
    a.reverse()
    return a

n = int(input("Enter limit: "))
a = list(map(int, input().split()))
r = great(n,a)
for _ in r:
    print(_,end="")
