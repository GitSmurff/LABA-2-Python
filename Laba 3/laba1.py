
x = int(input("Введите число от 1 до 9: "))
if  x >= 1 and x <= 3:
    s =str(input("Введите строку: "))
    n = int(input("Введите число повторов строки: "))
    i = 0
    a = [ s for i in range(n)]
    print(a)
            
elif x >= 4 and x <= 6:
    m = int(input("Введите степень, в которую следует возвести число: "))
    p = [x**m for i in range(1)]
    print(p)
elif x >= 7 and x <= 9:
    i = 0
    while i < 10:
         x += 1
         i += 1
         print(x)
else:
    print("Ошибка ввода!") 

