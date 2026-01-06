d={
    1:20,
    2:31,
    3:48,
    4:29

}

max,min=float('-inf'),float('inf')

for i in d:
    if d[i]>max:
        max=d[i]
    if d[i]<min:
        min=d[i]
print(max)
print(min)
    
