def one_appr(n,a):
    for i in range(n): 
        for j in range(n): 
            if (i != j):
                if (a[i] == a[j]): 
                    break
            j += 1
        if (j == n): 
            return a[i] 

n = int(input("Enter Limit: "))
a = list(map(int, input().split()))
r = one_appr(n,a)
print(r)
