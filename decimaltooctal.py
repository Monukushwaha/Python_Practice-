#convert decimal to binary  using python programme
num=int(input("enter decimal number : "))
while num>=1:
	print(num%8,end="")
	num=num//8


