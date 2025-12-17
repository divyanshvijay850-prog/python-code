my_list=[5,8,6,7,9,10]
for i in range(len(my_list)-1):
  for j in range(i+1,len(my_list)):
    if my_list[i]>my_list[j]:
      my_list[i],my_list[j]=my_list[j],my_list[i]
print(my_list)

