# # Tuples- Tules are orderd of cllection of elements 
# #tuples are immutable in nature .once you have created a tuple it can't be changed  after the creation of the tuple.
# # tuples are initialization with  parenthesis but there should minimum
# # one eleement and one comma..
# # t=(1,2,3,4)
# # print(type(t))

# # t=(2)
# # print(type(t))

# # initialising the tuple with one element
# # one element with comma
# # t=(5,)
# # print(type(t))

# #tuples are faster then list
# # Tuples are immutables  

# t=(1,2,3,4)
# print(t[0])

# Tuple packing- tuple packing is the process of grouping  values into a single tuple object in python
# in python this happens automatically whenever multiple comma -spreated values are assigned to a single variable name with or without parentheses

# vars=1,2,3
# print(type(vars))

# here the list is changed not  the tuple .here the whole list is considered as one element.

# t=([1,2],[3,4])
# t[0][1]=100
# print(t)

# vars=1,2,3
# a=vars[0]
# b=vars[1]
# c=vars[2]

# print(a)
# print(b)
# print(c)

#tuple unpacking-  Tuple unpacking also know as multiple assingment ir iterable unpacking is a powerfull python feature that allows you to assign the individual eleemnts of a tuple
# (or any other iterable like alist or string) to multiple variables in a single line of code.

# vars=1,2,3
# a,b,c=vars

# print(a,b,c)

# t=(1,2,2,2,3,4,5)
# # since the tuples are immutable so,it has only two methods 
# #1. count- which is used to find the frequency of the element .
# #1. index- it is used find the index of the element
# print(t.count(2))
# print(t.index(5))

# t1=(1,2,3)
# t2=(4,5,6)
# # IN concatenation of the tuple when we concat the two tuples then it from  a new tules.
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2)


