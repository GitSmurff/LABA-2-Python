class Zadanie:
    def __init__(self, x):      
        self.p = x
    def gg(self):
        if  self.p >= 1 and self.p <= 3:
            s =str(input("Введите строку: "))
            n = int(input("Введите число повторов строки: "))
            i = 0
            while i < n:
                print (s)
                i += 1
        return self.p
    def gg1(self):
        if self.p >= 4 and self.p <= 6:
             m = int(input("Введите степень, в которую следует возвести число: "))
             print(self.p**m)
        return self.p
    def gg2(self):
        if self.p >= 7 and self.p <= 9:
            i = 0
            while i < 10:
                self.p += 1
                i += 1
                print(self.p)
        return self.p
p = int(input())
a = Zadanie(p)
a.gg()
p = int(input())
a = Zadanie(p)
a.gg1()
p = int(input())
a = Zadanie(p)
a.gg2()
