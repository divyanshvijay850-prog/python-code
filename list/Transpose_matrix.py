li=[[1,2,3],[4,5,6],[7,8,9]]
transpose_matrix=[]
for i in range(len(li)):
  row=[]
  for j in range(len(li[i])):
    row.append(li[j][i])
  print()
  transpose_matrix.append(row)
print(transpose_matrix)
