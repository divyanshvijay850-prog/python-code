my_list=[1,2,2,3,4,4,5]
new_list=[]
for i in range(len(my_list)):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
print(new_list)