# create the multiplication table (from 1 to 10) of a number.
num=int(raw_input("enter number which you want table "))
for i in range(1,11):
	mul=i*num
	print(str(num)+' * '+str(i) + ' = ' + str(mul))
