#Python program to print alphabet pattern 'U'

for i in range(1,8):
	for j in range(1,8):
		if (i<=6 and (j==2 or j==3 or j==4)) or (i==7 and (j==1 or j==5)):
			print(" ",end="")
		elif(i<8 and j<=5):
			print("*",end="")
	print()
