
class Zadanie:
    cnt = 0
    def __init__(self):
        self.x = int(input('Введите число от 1 до 9: '))
    def gg(self):
        if  self.x >= 1 and self.x <= 3:
            s =str(input("Введите строку: "))
            n = int(input("Введите число повторов строки: "))
            i = 0
            while i < n:
                print (s)
                i += 1
        return self.x
    def gg1(self):
        if self.x >= 4 and self.x <= 6:
            m = int(input("Введите степень, в которую следует возвести число: "))
            print(self.x**m)
        return self.x
    def gg2(self):
        if self.x >= 7 and self.x <= 9:
            i = 0
            while i < 10:
                self.x += 1
                i += 1
                print(self.x)
            return self.x
    def gg3(self):
        if(self.x <=0 and self.x >= 10):
            print("Ошибка ввода!")
        return self.x
s = Zadanie()
Zadanie.gg(s)
Zadanie.gg1(s)
Zadanie.gg2(s)
Zadanie.gg3(s)
s.cnt = 9
for i in range(s.cnt):
    s = Zadanie()
    Zadanie.gg(s)
    Zadanie.gg1(s)
    Zadanie.gg2(s)
    Zadanie.gg3(s)


 



      




