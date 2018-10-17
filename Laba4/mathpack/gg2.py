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
