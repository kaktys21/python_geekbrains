'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

seconds = int(input("Seconds: "))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds = seconds - (hours * 3600 + minutes * 60)

if hours > 24:
    hours = 24

print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
