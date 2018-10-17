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
