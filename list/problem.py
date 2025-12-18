# # Intermediate
# # 9. Move all zeroes to the end of a list.
# # my_list=[1,2,3,0,0,5,6,7,0,8]
# # new_list=[]
# # for i in range(len(my_list)):
# #     if my_list[i]>0:
# #         new_list.append(my_list[i])

# # zero_count = my_list.count(0)
# # for i in range(zero_count):
# #     new_list.append(0)

# # print(new_list)


# # 10. Find the second largest element in a list.
# # my_list=[20,30,40,50,60,70,80]
# # first_largest=0
# # second_largest=0
# # for i in range(len(my_list)):
# #     if my_list[i]>first_largest:
# #         second_largest=first_largest
# #         first_largest=my_list[i]
# #     elif second_largest<my_list[i] and my_list[i] !=first_largest:
# #         second_largest=my_list[i]
# # print(second_largest)    



# # 11. Rotate a list to the right by 1 position.
# my_list=[1,2,3,4,5]
# k=my_list[-1]
# for i in range(len(my_list)-1,0,-1):
#     my_list[i]=my_list[i-1]

# my_list[0]=k
# print(my_list)

# # 12. Check if a list is a palindrome.
# # my_list=[1,2,3,2,1]
# # start=0
# # end=len(my_list)-1
# # b= True
# # while start<end:
# #      if my_list[start]!=my_list[end]:
# #           b=False
# #           break
# #      start+=1
# #      end-=1
# # if b == True:
# #      print("pailndrome")
# # else:
# #      print("not pailndrome")



# # 13. Split a list into two halves.

# # my_list=[10,20,30,40,50,60]
# # a,b=[],[]
# # half=len(my_list)//2
# # for i in range(half):
# #     a.append(my_list[i])
# #     b.append(my_list[half+i])
# # print(a,b)
    
       

# # 14. Find common elements between two lists.
# a=[1,2,3,4,5]
# b=[2,8,3,9,6]
# for i in range(len(a)):
#     if a[i]==b[i]:
#         print(a[i])



 # 15. Replace all negative numbers in a list with 0.

# my_list=[1,2,3,-4,5,-6,7,-8,9]
# for i in range(len(my_list)):
#     if my_list[i]<0:
#         my_list[i]=0
# print(my_list)
    

