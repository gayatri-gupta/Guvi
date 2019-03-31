n = int(input())

t = n 
rv = 0
while(n>0):
    d = n%10
    rv = rv*10+d
    n = n//10
    
if rv ==t:
    print("yes")
else:
    print("no")
