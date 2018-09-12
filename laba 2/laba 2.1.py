s = input("Введите строку: ").split()
c = 0
for i in s:
    if len(i) > c:
        c = len(i)
        k = i
print("Самое длиное слово в строке: ", k)
