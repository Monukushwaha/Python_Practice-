# programme for  print pattern of alphabate P:

for i in range(1,8):
	for j in range(1,8):
		if (i==1 and j==5) or ((i==2 or i==3) and (j==2 or j==3 or j==4)) or ((i==5 or i==6 or i==7) and (1<j)) or (i==4 and j==5):
			print(" ",end="")
		elif(i<8 and j<=5):
			print("*" ,end="")
	print()

