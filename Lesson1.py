# задание №1
duration = int(input('Веди время в секундах'))

days = duration // 86400  # 86400 - это количество секунд в сутках, вычисляем кол-во суток
hours = (duration - days * 86400) // 3600  # 3600 количество секунд в часе, вычисляем кол-во часов
minutes = (duration - days * 86400 - hours * 3600) // 60  # Вычисляем кол-во минут
seconds = duration - days * 86400 - hours * 3600 - minutes * 60

if duration >= 86400:
    print('Вы ввели', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    print('Вы ввели', hours, 'час', minutes, 'мин', seconds, 'сек')
elif 60 <= duration < 3600:
    print('Вы ввели', minutes, 'мин', seconds, 'сек')
else:
    print('Вы ввели', duration, 'сек')

# задание №2

numbers = list(range(1, 101, 2))
print(numbers)
# cube_numbers = []
# seven_numbers = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 != 0:
#         number = numbers[i] ** 3
#         cube_numbers.append(number)
#
# print(cube_numbers)
# #numbr = 0
#
# for x in range(len(cube_numbers)):
#     operand = list(str(cube_numbers[x]))
#     for y in range(len(operand)):
#         numbr = numbr + int(operand[y])
#         seven_numbers.append(numbr)
# print(seven_numbers)





