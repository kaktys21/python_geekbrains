'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

def TwoDigits(num):
    return str(num) if num >= 10 else '0' + str(num)

seconds = int(input("Seconds: "))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - (hours * 3600 + minutes * 60)

if hours > 24:
    hours = 24

print('{}:{}:{}'.format(TwoDigits(hours),TwoDigits(minutes),TwoDigits(seconds)))