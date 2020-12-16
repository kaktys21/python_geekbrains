'''Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.'''

prof, costs = int(input('Enter profit: ')), int(input('Enter costs: '))
if prof > costs:
    print('Profit!\nProfitability: {}'.format(prof/costs))
    people = int(input('Enter num of employees: '))
    print('Profit/pople: {}'.format(prof/people))
elif profit == costs:
    print('Zero profit')
else:
    print('Your treasury is empty, my lord!')
