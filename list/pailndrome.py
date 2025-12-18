mylist=[1,2,3,4,3,2,1]
start=0
end=len(mylist)-1
b=True
while start<end:
  if mylist[start]!=mylist[end]:
    b=False
    break
  start+=1
  end-=1
if b==True:
  print("pailndrome")
else:
  print("not pailndrome")


#   #2 method 

# lis=[1,2,3,4,3,2,1]

# b=True
# n=len(lis)

# for i in range(n //2):
#   if lis[i]!=lis[n-1-i]:
#     b=False
#     break
# if b:
#   print("pailndrome")
# else:
#   print("not pailndrome")
