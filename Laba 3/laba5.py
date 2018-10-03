
def gg():
    x = int(input("Введите число от 1 до 3: "))
    if  x >= 1 and x <= 3:
        s =str(input("Введите строку: "))
        n = int(input("Введите число повторов строки: "))
        i = 0
        while i < n:
            print (s)
            i += 1
    else:
        print("Ошибка ввода!")

def gg1():
    x = int(input("Введите число от 4 до 6: "))
    if x >= 4 and x <= 6:
        m = int(input("Введите степень, в которую следует возвести число: "))
        print(x**m)
    else:
        print("Ошибка ввода!")
    
def gg2():
    x = int(input("Введите число от 7 до 9: "))
    if x >= 7 and x <= 9:
        i = 0
        while i < 10:
            x += 1
            i += 1
            print(x)
    else:
        print("Ошибка ввода!") 
   




