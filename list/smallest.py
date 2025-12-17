my_list=[20,30,40,10,50,60]
smallest=float('inf')
for i in range(len(my_list)):
    if my_list[i]<smallest:
        smallest=my_list[i]
print(smallest)
