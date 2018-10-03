x = int(input())
def add():
    global x
    if x >= 0 and x <= 7:
        print("Вам в детский сад")
add()

def add1():
    global x
    if x > 7 and x <= 18:
        print("Вам в школу")
add1()
def add2():
    global x
    if x > 18 and x <= 25:
        print("Вам в профессональное учебное заведение")
add2()
def add3():
    global x
    if x > 25 and x <= 60:
        print("Вам на работу")
add3()
def add4():
    global x
    if x > 60 and x <= 120:
        print("Вам предоставляется выбор")
add4()
def add5():
    global x
    if x < 0 or x > 120:
        for i in range(5):
            print("Ошибка! Это программа для людей!")
add5()
