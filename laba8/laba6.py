import datetime
fmt = '%Y.%m.%d'
s = str(input())
dt = datetime.datetime.strptime(s, fmt)
tt = dt.timetuple()
print(tt.tm_yday)
