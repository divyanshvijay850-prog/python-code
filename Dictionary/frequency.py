st='pineapple'
freq={}
for c in st:
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1
for key in freq:
    if freq [key]>=2:
        print(key,freq[key])