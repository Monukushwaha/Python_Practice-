#programme for find the  season for that month and day.
month=raw_input(" input the month between january - Decemeber : ")
day_number=int(input("enter number of days"))
if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if month=='March' and day_number>15:
	season='spring'
elif month=='June' and day_number>15:
	season="summer"
elif month=='September' and day_number>15:
	season="autumn"
elif month=='December' and day_number>15:
	season="winter"

print("season is " + season )
