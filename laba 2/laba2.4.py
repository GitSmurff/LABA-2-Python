S1 = input("Введите строку: ").split()
S2 = input("Введите слово: ")
C = S1.count(S2)
if C == 0:
    print("Такого слова нет.")
else:
    print("Есть такое слово.") 
