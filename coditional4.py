num=1
num += int(input("enter number which we want pattern"))
for i in range(1 ,num):
	for j in range(1,i,1):
		print ("*",end="")

	print()

for i in range(num,1,-1):
	for j in range(1,i,1):
		print("*",end="")
	print()
