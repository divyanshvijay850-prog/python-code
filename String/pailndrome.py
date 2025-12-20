# # Write a program to check whether a given string is a palindrome or not.
# text="saras"
# if text==text[::-1]:
#   print("pailndrome")
# else:
#   print("not Pailndrome")

# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('enter the string')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Not a Palindrome')
    break

if flag:
  print('Palindrome')

