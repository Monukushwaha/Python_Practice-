#Python program to print alphabet pattern 'Z'.

for i in range(1,8):
	for j in range(1,8):
		if (i==2 and j!=6) or (i==3 and j!=5) or (i==4 and j!=4) or (i==5 and j!=3) or (i==6 and j!=2):
			print(" ",end="")
		elif(i<8 and j<8):
			print("*",end="")
	print()
