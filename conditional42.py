#calculate the sum and average of n integer numbers.
sum=0
num=int(raw_input("enter number for sum and average : "))
for i in range(1,num+1):
	sum=sum+i
print("the sum of number till " + str(num) + " is " + str(sum) + " and average of number is  " + str(sum/num))
