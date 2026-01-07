my_dict={
    1:20,
    2:30,
    3:40,
    4:60

}
first_largest,second_largest=float('-inf'),float('-inf')
for i in my_dict:
    if my_dict[i]>first_largest:
        second_largest=first_largest
        first_largest=my_dict[i]
    elif my_dict[i]>second_largest:
        second_largest=my_dict[i]

print(second_largest)
    