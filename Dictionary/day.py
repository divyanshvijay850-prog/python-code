# # Dictionary is a data type in python which stores the key and value pairs .
# # dictionary is mutable
# # keys must be unique and also keys are immutabe
# # d={}
# # print(type(d))

# student_data={
#     'name': 'Ram',
#     'class': 'A23',
#     'roll no':25
# }

# print(student_data)

# # The value of any key is accessed by that key

# #  d={key : value}
# # so the basic syntax of dictionary is dic ={key:value}


# #syntax dict(key=value)
# # dict(name='rahul',rollno=25,batch='A24')

# data={
#     'name':['ram','shayam','naman'],
#     'roll no':[20,25,30]

# }

# print(data['roll no'][0])

# # To access any value we can also use .get() method byt there is a small using this []and .get()
# # in square brackets it would give error if the key is not present in to dictonary 
# # but into the get () method it would not give any error

# # student_data.keys()
# #student_data.values()

# for key in student_data:
#     print(f'{key}-> {student_data[key]}')


# student_data={
#     'name':'Ram',
#     'Age' : 25,
#     'rollno': 'A24'
# }

# for key ,value in student_data.items():
#     print(f'{key}-> {value}')


# my_dict={'key':'value'}

# #acesss element from the dictionary
# my_dict['key']
# print(my_dict['key'])

# #Accessing the element from the dictionary using the function
# my_dict.get['key']

# student_data={
#     'name':'Divyansh',
#     'Batch':'A23',
#     'Location':'jaipur'

# }

# print(student_data['name'])

# #student_data['city]

# print(student_data.get('city','rajesthan'))


# dict(name='aman',batch='A1',rollno=20)


student_data={
    'name':'Divyansh',
    'Batch':'A23',
   'Location':'jaipur',
   'mobile': 894942

 }

# student_data['mobile']=8949429742
# print(student_data)

# add one more key - value into this dictionary
# student_data['Addresss']='jaipur'

# print(student_data)

#.update method is used to add the more key value pairs into the dictionary

# student_data.update({'roll no':25,'vehicle':'Bike'})
# print(student_data)


# .keys method is used to get all the keys of the dictionary.

# print(student_data.keys())

# create a dictionary using two list

# keys=['name','Batch','rollno']
# values=['Rohan','A23',35]
# new_dict={}

# for i in range(len(keys)):
#     new_dict[keys[i]]=values[i]

# print(new_dict)


# print key value pairs using the for loop

# for i,j in new_dict.items():
#     print(i,j)

s= "This is a sentence  This is a sentence".split()
d={}

for i in range(len(s)):
    word=s[i]
    if word in d:
        d[word]+=1
    else:
        d[word]=1

print(d)




     
