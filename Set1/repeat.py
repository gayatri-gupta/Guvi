def repeat(N,x):  
    repeated = [] 
    for i in range(N): 
        k = i+1
        for j in range(k, N): 
            if x[i] == x[j]:
                if x[i] not in repeated: 
                    repeated.append(x[i]) 
    return repeated

N = int(input("Enter limit: "))
a = list(map(int,input("Values are: ").split()))
r = repeat(N,a)
if r==[]:
    print("unique")
else:    
    for _ in r:
        print(_,end=" ")