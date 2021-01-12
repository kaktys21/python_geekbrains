'''4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.'''

alp = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('123.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    

with open('123rus.txt', 'w', encoding = 'utf-8') as output:
    for line in lines:
        s = line.split(' — ')
        output.write(alp[s[0]] + ' — ' + s[1])
