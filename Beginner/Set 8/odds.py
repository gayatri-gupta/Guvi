try:
    s = input()
    for i in s:
        if int(i)%2!=0:
            print(i,end=" ")
except ValueError:
    print("Invalid Input")
