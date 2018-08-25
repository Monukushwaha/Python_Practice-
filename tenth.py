number=input("enter the number :- ")
for i in range(2,number-1):
	if number % i !=0:
		continue
	elif number % i==0:
		print("number is not prime")

	print("not prime ")
