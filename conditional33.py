#convert month name to a number of days
d={'January':31, 'February':28/29, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 
'November':30, 'December':31}
month=raw_input("enter the month which you wants number of days : ")
if  month in d:
	print(d[month])
