import codecs
import json
menu = input("Введите 1, чтоб вывести все товыры которые считаются парами\nВведите 2, чтоб вывести все товары которые считаются штуками\nВведите 3, чтоб подсчитать количество товары которых хронятся в парах, и по одному\n>>> ")
shop = open('LetsPlay.json', 'r+', encoding='utf-8')
one = 0
two = 0
oneall = 0
twoall = 0
test = ""
for line in shop:
    c = 0
    for i in range(0, len(line)):
        if(i <= len(line)):
            if(menu == '1' and c == 0 and line[i] == '"' and line[i+1] == 't' and  line[i+2] == '"'):
                line = line.replace(';', '')
                line = line.replace(',"t"', '')
                line = line.replace('"', '')
                line = line.replace(',', ', ')
                line = line.replace('\n', '')
                line = line.replace('	', '')
                c = c + 1
                test = [int(s) for s in line.split() if s.isdigit()]
                r = int("".join(map(str, test)))
                twoall = twoall + r
                r = r * 2
                print(line + " пар = " + str(r) + " едениц")
            elif(menu == '2' and c == 0 and line[i] == '"' and line[i+1] == 'o' and  line[i+2] == '"'):
                line = line.replace(';', '')
                line = line.replace(',"o"', '')
                line = line.replace('"', '')
                line = line.replace(',', ', ')
                line = line.replace('\n', '')
                line = line.replace('	', '')
                c = c + 1
                test = [int(s) for s in line.split() if s.isdigit()]
                r = int("".join(map(str, test)))
                oneall = oneall + r
                print(line + " едениц")
            elif(menu == '3' and c == 0):
                if (line[i] == '"' and line[i+1] == 'o' and  line[i+2] == '"'):
                    one = one + 1
                elif(line[i] == '"' and line[i+1] == 't' and  line[i+2] == '"'):
                    two = two + 1
if (menu == '3'):
    print("Товаров которые хронятся в парах: " + str(two) + "\nТоваров которые хронятся штучно: " + str(one))
    json.dump('{' + "all two=" + str(two) + " all one=" + str(one) + '}', shop)
elif (menu == '1'):
    print("Всего едениц товара в парах: " + str(twoall))
elif (menu == '2'):
    print("Всего едениц товара в еденицах: " + str(oneall))
shop.close()
