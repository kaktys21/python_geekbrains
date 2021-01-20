import json

profit = dict()
prof = 0
i = 0
f = []

with open('firms.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        profAver = prof / i
    pr = {'AverProf': round(profAver)}
    f.append(profit)
    f.append(pr)

with open('firms.json', 'w') as writejs:
    json.dump(f, writejs)

print(f)
    