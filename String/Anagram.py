# words = ["eat", "tea", "ate", "bat", "tab"]
# result = []

# for word in words:
#     found = False
#     for group in result:
#         if sorted(word) == sorted(group[0]):
#             group.append(word)
#             found = True
#             break
#     if not found:
#         result.append([word])

# print(result)

# li = ['ate', 'eat', 'nap', 'pan']
# di = {}
# li1 = []
# for i in range(len(li)):
#   word = ''.join(sorted(li[i]))
#   if word not in di:
#     di[word] = [li[i]]
#   else:
#     di[word].append(li[i])
  
# for i in di:
#   li1.append(di[i])
# print(li1)
