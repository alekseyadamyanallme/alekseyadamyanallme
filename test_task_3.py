
points = int(input()) #вводим количество баллов
if points in range(1, 101):
    print('Скидка 1%')
elif points in range(101, 201):
    print('Скидка 3%')
elif points in range(201, 501):
    print('Скидка 5%')
elif points >=501:
    print('Скидка 10%')
else:
    print('У Вас нет скидки')
