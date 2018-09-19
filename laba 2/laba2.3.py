S1 = input("Введите строку: ").split()
S2 = input("Введите знак: ")
for i in range (len(S1)):
    for j in range (len(S1[i])):
        if S1[i][j] == S2:
            print("Ваше слово: ", S1[i])





