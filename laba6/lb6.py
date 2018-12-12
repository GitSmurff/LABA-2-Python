from abc import ABC,abstractmethod,abstractproperty

class dz(ABC):
    @abstractmethod
    def __init__(self,x):
        x=0
        self.x=x
class main(dz):
    def __init__(self,x):
        self.x=x;
class pack(main):
    def gg1(self):
        if  x >= 1 and x <= 3:
            s =str(input("Введите строку: "))
            n = int(input("Введите число повторов строки: "))
            i = 0
            while i < n:
                print (s)
                i += 1
    def gg2(self):
        if x>=4 and x<=6:
            m = int(input("Введите степень, в которую следует возвести число: "))
            print(x**m)
            
    def gg3(self):
        if x>=7 and x<=9:
            tmp=x
            for i in range(10):
                tmp+=1
                print(tmp)
                
x=int(input())
a=pack(x)
while x!=0:
    if x>=1 and x<=3:
        a.gg1()
    elif x>=4 and x<=6:
        a.gg2()
    elif x>=7 and x<=9:
        a.gg3()
    else:
        print('Ошибка')
    x=int(input())
    a=pack(x)
