import re
f = open('text.txt')
data = f.read()
print(data)
with open('text.txt') as f:
    k = sum(1 for _ in f)
summ = 0
data = re.findall(r'\-\d+', data)
data = [int(x) for x in data]
for x in data:
    summ +=x
sumn=0
f = open('text.txt')
dat = f.read()
dat = re.findall(r'\-\d', dat)
dat = [int(y) for y in dat]
for y in dat:
    sumn +=y
print('Кол-во товаров:', k, ' Кол-во штук',summ, 'Кол-во пар',sumn)
f.close()
f = open('text.txt','a')
f.write(str(k)+ '\t' + str(summ) + '\t' + str(sumn))
f.close()
