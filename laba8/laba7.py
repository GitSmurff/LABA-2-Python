import datetime
from datetime import datetime, timedelta
data = str(input())
date = datetime(day=int(data[0:2]), month=int(data[2:4]), year=int(data[4:8]))
data = date.strftime("X%d/%B/%y").replace('X0','X').replace('X','')
print(data)
