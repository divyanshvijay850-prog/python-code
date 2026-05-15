 list=[2,20,15,7,11]

# i,j=0,1

# while(i<len(list)-1 and j<len(list)-1):
#     if list[i]>list[j]:
#         list[i],list[j]=list[j],list[i]
#     j+=1

#     if j==len(list)-1:
#         i+=1
#         j=i+1
# print(list)



li=[5,4,1,3,2]

start=0
end=1
n=len(li)

while end<n:
    if li[end]>li[start]:
        li[start],li[end]=li[end],li[start]
        start=0
        end=1
    else:
        start+=1
        end+=1
print(li)

