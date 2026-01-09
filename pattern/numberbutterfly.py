n=5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    for k in range(2*n-2*i):
        print("-",end=" ")
    for e in range(i):
        print(i,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print(i,end=" ")
    for k in range(2*n-2*i):
        print("-",end=" ")
    for e in range(i):
        print(i,end=" ")
    print()

