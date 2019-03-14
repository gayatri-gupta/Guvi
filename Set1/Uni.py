t = int(input())

l = list(map(int,input().split()))

r = []
for i in l:
    if i in r:
        print(i)
        break
    
    else:
        r.append(i)

if len(set(l))==t:
    print("unique")

    
