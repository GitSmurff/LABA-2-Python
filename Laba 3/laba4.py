x = 0
y = 1
def add():
    global x, y
    x = y
    y +=1
    z = y**x
    print(y, " ", x, " ", z)
   
for i in range(10):
    add()
    


