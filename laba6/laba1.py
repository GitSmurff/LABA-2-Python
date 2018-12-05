import abc
class Abstract(abc.ABC):
    @abc.abstractmethod
    def __init__(self, x):
        self.x = 0
class Queen(Abstract):
    def __init__(self):
        self.x = int(input('Введите число от 1 до 9: '))
        if  self.x >= 1 and self.x <= 3:
            s =str(input("Введите строку: "))
            n = int(input("Введите число повторов строки: "))
            i = 0
            while i < n:
                print (s)
                i += 1
        elif self.x >= 4 and self.x <= 6:
            m = int(input("Введите степень, в которую следует возвести число: "))
            print(self.x**m)
        elif self.x >= 7 and self.x <= 9:
            i = 0
            while i < 10:
                self.x += 1
                i += 1
                print(self.x)
        else:
            print("Ошибка ввода!")
        return self.x
x = Queen()






