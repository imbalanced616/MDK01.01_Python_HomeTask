print()  # Пирамида
print("Задача №2.\nВыберите способ реализации задачи.\nДля этого введите цифру выбранного цикла:\n1. while\n2. for")
print()

sel_numb = int(input())
print()

print("Введите высоту пирамиды:", end=' ')
n = int(input())
if sel_numb == 1:
    spase = n - 1
    star = 1
    j = 0
    while j < n:
        print(' ' * spase + '*' * star)
        star += 2
        spase -= 1
        j += 1
elif sel_numb == 2:
    spase = n - 1
    star = 1
    for i in range(1, n + 1):
        print(' ' * spase + '*' * star)
        star += 2
        spase -= 1
else:
    input("Ошибка! Неверный ввод.")
