import datetime

year, month, day = input().split()

date =datetime.date(int(year), int(month), int(day))
days_var = int(input())
date =date + datetime.timedelta(days= days_var)
print (date.year, date.month, date.day)
