num=(1,2,3,4,5,6,7,8,9,12,23)
count=0
od_count=0
for i in num:
	if i%2==0:
		count=count+1
	else:
		od_count=od_count+1
print("total even number in the series " + str(count))
print("total odd number in the series " + str(od_count))

