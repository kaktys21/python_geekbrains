'''Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.'''

def NotChitInsert(rate, value):
    maxValue = max(rate)
    if value > maxValue:
        rate.insert(0, value)
    elif value in rate:
        rate.insert(rate.index(value) + rate.count(value), value)
    else:
        rate.append(value)
    return rate

def ChitInsert(rate, value):
    rate.append(value)
    rate.sort(reverse = True)
    return rate


rate = [7, 6, 5, 5, 4, 3, 3, 3, 2, 1]

while True:
    try:
        newNum = int(input('Enter num. Not num to stop: '))
    except:
        break
    #rate = ChitInsert(rate, newNum)
    rate = NotChitInsert(rate, newNum)
    print(rate)
else:
    print(f'Final rate:\t{rate}')