import datetime
year=int(raw_input("input year : "))
month=int(raw_input("input month : "))
day=int(raw_input("input day : "))
date = datetime.datetime(year,month,day)
date += datetime.timedelta(days=1)
print(date)

