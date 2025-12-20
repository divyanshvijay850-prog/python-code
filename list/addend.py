#Write a program to move all zeros in a list to the end without changing the order of
# non-zero elements.

my_list=[1,2,3,0,0,0,4,5,6]
new_list=[]
for i in range(len(my_list)):
    if my_list[i] >0:
      new_list.append(my_list[i])

Zero_count=my_list.count(0)

for i in range(Zero_count):
    new_list.append(0)
print(new_list)


