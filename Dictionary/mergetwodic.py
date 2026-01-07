# a={'a':1,'b':2,'c':3}
# b={'d':4,'e':5,'f':6}

# for key in b:
#     a[key]=b[key]
# print(a)

# a.update(b)
# print(a)


a={'a':1,'b':2,'c':3}
b={'d':4,'e':5,'f':6}

d={**a,**b}

print(d)



        
