import math

print()  # Потепление
print("Задача №4.\nВыберите способ реализации задачи.\nДля этого введите цифру выбранного цикла:\n1. while\n2. for")
print()

sel_numb = int(input())
print()

print("Введите целое количество дней:", end=' ')
n = int(input())
count = 0
week = 0
print("Введите температуру за каждый день:")
if sel_numb == 1:
    i = 1
    temp = []
    while i <= n:
        temp.append(float(input(str(i) + ': ')))
        if temp[i - 1] < 23:
            count += 1
        else:
            break
        i += 1
    week = math.floor(count / 7)
    print("Количество полных недель, до того дня как температура стала больше или равна 23 гр. Цельсия:", week)
elif sel_numb == 2:
    temp = []
    for i in range(1, n + 1):
        temp.append(float(input(str(i) + ': ')))
        if temp[i - 1] < 23:
            count += 1
        else:
            break
    week = math.floor(count / 7)
    print("Количество полных недель, до того дня как температура стала больше или равна 23 гр. Цельсия:", week)
