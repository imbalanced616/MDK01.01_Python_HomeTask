print()  # Запуск ракеты
print("Задача №1.\nВыберите способ реализации задачи.\nДля этого введите цифру выбранного цикла:\n1. while\n2. for")
print()

sel_numb = int(input())
print()

print("Введите целое количество секунд:", end=' ')
n = int(input())
if sel_numb == 1:
    while n != -1:
        print('Осталось секунд:', n)
        n -= 1
    print('Пуск')
elif sel_numb == 2:
    for i in range(n, -1, -1):
        print('Осталось секунд:', i)
    print('Пуск')
else:
    input("Ошибка! Неверный ввод.")
