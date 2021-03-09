import datetime
date = "08/03/2021 21:51:18"
day = int(date[0]+date[1])
month = int(date[3]+date[4])
year = int(date[6]+date[7]+date[8]+date[9])

date = datetime.datetime(year, month, day)
date1 = datetime.datetime(2021, 2, 3)

print("d1 is greater than d : ", date1 > date)


