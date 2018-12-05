import datetime
from datetime import datetime, timedelta, date
now_date = date.today()
print("Текущая дата: ",now_date)
cur_month = now_date.month
d = date.today() - timedelta(cur_month)
print(d)
dd = date(d.year+1, d.month, d.day)
print(dd)

