words=['eat','ate','tea','silent','listen']

new_dict={}

for word in words:
    result=''.join(sorted(word))

    if result not in new_dict:
        new_dict[result]=[]
    new_dict[result].append(word)

print(new_dict)
