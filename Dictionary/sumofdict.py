d={'a':(1,2,3),'b':(4,5),'c':(6,7)}
new_dict={}
for key ,Values in d.items():
    new_dict[key]=sum(Values)
print(new_dict)

