# Write a program to find the frequency of each character in a given string.
a="programming"
freq={}
for ch in a:
  if ch in freq:
    freq[ch]+=1
  else:
    freq[ch]=1
print(freq)