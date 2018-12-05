import datetime
from datetime import datetime, timedelta
data = str(input())
date = datetime(year=int(data[0:4]), month=int(data[4:6]), day=int(data[6:8]))
data = date.strftime("%Y-%m-%d")
print(data)
