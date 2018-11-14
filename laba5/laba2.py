class Zadanie2:
    cnt = 0
    def __init__(self):
        self.x = int(input('Введите число от 1 до 9: '))
    def gg(self):
        print("Общество в начале XXI века")
        if self.x >= 0 and self.x <= 7:
            print("Вам в детский сад")
        elif self.x > 7 and self.x <= 18:
            print("Вам в школу")
        elif self.x > 18 and self.x <= 25:
            print("Вам в профессональное учебное заведение")
        elif self.x > 25 and self.x <= 60:
            print("Вам на работу")
        elif self.x > 60 and self.x <= 120:
            print("Вам предоставляется выбор")
        elif self.x < 0 or self.x > 120:
            for i in range(5):
                print("Ошибка! Это программа для людей!")
        return self.x
s = Zadanie2()
s.gg()
s.cnt = 9
for i in range(s.cnt):
    s = Zadanie2()
    s.gg()
    
