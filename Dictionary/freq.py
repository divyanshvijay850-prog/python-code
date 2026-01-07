# li=[1,1,2,3,4,3]
# freq={}

# for i in range(len(li)):

#     if li[i] in freq:
#         freq[li[i]]+=1
#     else:
#         freq[li[i]]=1
# print(freq)
    
li=[1,2,2,3,4,3]
freq={}
for i in range(len(li)):
    freq[li[i]]=freq.get(li[i],0)+1
print(freq)
