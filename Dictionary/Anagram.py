# worda='ate'
# wordb='eat'
# d=True
# for c in worda:
#     if c not in wordb:
#         print("not Anagram")
#         d=False
#         break
# if d:
#     print("anagram")

# word1="eat"
# word2="ate"

# if sorted(word1)==sorted(word2):
#     print("anagram")
# else:
#     print("not anagram")


# words = ["eat", "tea", "ate", "bat", "tab"]
# anagrams = {}

# for word in words:
#     key = ''.join(sorted(word))
#     anagrams.setdefault(key, []).append(word)

# print(list(anagrams.values()))


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


# li = ['ate', 'eat', 'nap', 'pan']
# li1 = []
# a = []
# for i in range(len(li)-1):
#   if li[i] in a:
#     continue
#   l = [li[i]]
#   for j in range(i+1,len(li)):
#     if sorted(li[i])==sorted(li[j]):
#       l.append(li[j])
#       a.append(li[j])
#   li1.append(l)
# print(li1)




