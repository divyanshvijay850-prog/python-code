# # # # # for i in range(1,6):
# # # # #     for j in range(1,i+1):
# # # # #         print(" ",end=" ")
# # # # #     for k in range(1,6-i+1):
# # # # #         print("*",end=" ")
# # # # #     print()
# # # # # n=5
# # # # # for i in range(1,n+1):
# # # # #     for j in range(n-i):
# # # # #         print(" ",end=" ")
# # # # #     for k in range(2*i-1):
# # # # #         print("*",end=" ")
# # # # #     print()

# # # # n=4
# # # # for i in range(1,n+1):
# # # #     for j in range(n-i):
# # # #         print(" ",end=" ")
# # # #     for k in range(2*i-1):
# # # #         print(k+1,end=" ")
# # # #     print()

# # # # n=4
# # # # for i in range(1,n+1):
# # # #     for j in range(1,n-i+1):
# # # #         print(" ",end=" ")
# # # #     for k in range(1,i+1):
# # # #         print(k,end=" ")
# # # #     for j in range(1,i):
# # # #         print(j,end=" ")
# # # #     print()

# # # # 

# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,n-i+1):
# #         print("-",end=" ")
# #     for j in range(2*i-1):
# #         print("*",end=" ")
# #     print()
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print("-",end=" ")
# #     for j in range(1,n-i):
# #         print("*",end=" ")
# #     for j in range(1,n-i+1):
# #         print("*",end=" ")
    

# #     print()

# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j== 2*i-1 :
#             print("*",end=" ")
#         else:
#print(" ",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(5,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#       if j==1 or j==2*i-1 :
#         print("*",end=" ")
#       else:
#           print(" ",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end="")
#     for k in range(i,7-1):
#         print(k,end=" ")
#     print()
# x=1
# for i in range(1,5):
#     for j in range(1,5-i):
#         print("-",end="")
#     for j in range(1,i+1):
#         print(x,end=" ")
#         x+=1
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print("-",end="")
#     for j in range(1,i+1):
#         if i==5 or j==1 or j==i :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# for i in range(1,5):
#     for j in range(1,6):
#       if i==1 or i==4 or j==5 or j==1:
#         print("*",end="")
#       else:
#          print(" ",end="")
#     print()

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

# ch=ord('E')
# for i in range(1,6):

#     for j in range(i):
#         print(chr(ch+j),end=" ")
#     ch-=1
    
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,6):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     x=65
#     for j in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,6):
#         print(chr(x),end=" ")
#         x+=1
#     print()

# n = 5

# for i in range(1, n+1):

#     print("  " * (n - i), end="")

#     for j in range(i, 2*i):
#         print(j, end=" ")

#     for j in range(2*i - 2, i - 1, -1):
#         print(j, end=" ")

#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#       if i==1 or i==j or i==5 or j==1:
#         print(j,end=" ")
#       else:
#          print(" ",end=" ")
#     print()

num=5
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for k in range(1,i+1):
      if k==1 or i==k:
        print("*",end=" ")
      else:
         print(" ",end=" ")
    
    print()
for i in range(1,num+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,num-i+1):
        if k==1 or k==num-i:
      
            print("*",end=" ")
        else:
           print(" ",end=" ")
    print()