import datetime
m = [31,28,31,30,31,30,31,31,30,31,30,31]
def f(day):
    month = 0
    for i in m:
        day -= i
        month += 1
        if day <= 0:
            return day+i,month

n = int(input())           
print(f(n))

