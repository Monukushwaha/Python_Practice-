#find numbers between 100 and 400 (both included) where each digit of a number is an even number
list=[]
for i in range(100,400):
	d=str(i)
	if (int(d[0])%2)==0 and (int(d[1])%2)==0 and (int(d[2])%2)==0:
		list.append(d)
print (",".join(list))
