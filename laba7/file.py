import re
fwr = open('price.txt','r')
file =fwr.read()
str(x) =re.findall(r'\d+шт',file)
y = re.findall(r'\d+пар',file)
"""sht_string = ''.join(x)         #Списки в строки
par_string = ''.join(y)
result_par = re.findall(r'\d+',par_string)   #Новый поиск
result_sht = re.findall(r'\d+',sht_string)
new_list_par = []
new_list_sht = []
for item in result_par:
    new_list_par.append(int(item))      #Из строки в инт
for item in result_sht:
    new_list_sht.append(int(item))
counter_sht =0
counter_par = 0
for item in new_list_sht:               #Подсчет
    counter_sht +=item
for item in new_list_par:
    counter_par +=item*2
print(file)
print("Количество пар в штуках: " + str(counter_par) +"; Количество штучных товаров: "+ str(counter_sht)+"\n")
fwr.close()"""
print(x)
print(y)
