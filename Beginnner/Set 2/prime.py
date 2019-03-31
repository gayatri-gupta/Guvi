import math as m
n = int(input())

def prime(n):
    for i in range(2,int(m.sqrt(n))+1):
        if n%i == 0:
            return False
        
    else:
        return True
    
x = prime(n)
if x is False:
    print("no")
else:
    print("yes")
