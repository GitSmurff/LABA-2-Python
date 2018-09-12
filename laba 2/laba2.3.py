s = input("Введите строку: ")
t = min(s.split(), key=len)
print("Самое короткое слово в строке: ", t)
