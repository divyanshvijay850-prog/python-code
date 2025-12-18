l1=[10,20,30,40,60,50]
first_largest=0
second_largest=0
for i in range(len(l1)):
  if l1[i]>first_largest:
    second_largest=first_largest
    first_largest=l1[i]
  elif l1[i]>second_largest:
    second_largest=l1[i]
print(second_largest)
