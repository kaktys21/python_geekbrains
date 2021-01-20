'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.'''

with open('table.txt', 'r', encoding = 'utf-8') as f:
    table = [(line.split()[0], int(line.split()[1])) for line in f.readlines()]
    
more = 0
for p in table:
    if p[1] > 20000:
        print(*p)
        
gen = [l[1] for l in table]
print(sum(gen)/len(gen))