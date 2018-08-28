mat=[]
for i in range(0,3):
	mat.append([])
for i in range(0,3):
	for j in range(0,4):
		mat[i].append(j)
		mat[i][j]=i*j
print(mat)
