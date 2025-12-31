# # num=6
# # for  i in range(1,num+1):
# #     for j in range(1,num+1):
# #         if i==1 or  i==num or j==1 or j==num:
# #          print("*",end="")
# #         else:
# #            print(" ",end="")
# #     print()
    
rows=4
column=6
for i in range(1,rows+1):
    for j in range(1,column+1):
        if i==1 or i==rows or j==1 or j==column:
            print("*",end="")
        else:
            print(" ",end="")
    print()

# for i in range(1,6):
#     x=65
#     for j in range(1,i+1):
#         print(chr(x),end=" ")
#         x+=1
#     print()

# x=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(x),end=" ")
#     x+=1
#     print()
