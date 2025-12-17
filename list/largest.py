my_list=[10,20,30,50,60,40]
largest=0
for i in range(len(my_list)):
    if my_list[i]> largest:
        largest= my_list[i]
print(largest)