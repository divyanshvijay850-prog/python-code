# Find the length of a given string without using the len() function

s = input('enter the string')

counter = 0

for i in s:
  counter += 1

print('length of string is',counter)