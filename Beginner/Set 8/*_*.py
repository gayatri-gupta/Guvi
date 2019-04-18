s = list(input())
l = len(s)
if l%2==0:
    a = l//2
    b = a-1
    s[a] = '*'
    s[b] = '*'
else:
    s[(l//2)] = '*'
for i in s:
    print(i,end="")
