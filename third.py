number=input("enter the number which you wants devisior :- ")
list=[]
i=1
while i<=number:
	if number % i==0:
		list.append(i)
	i=i+1
print list
