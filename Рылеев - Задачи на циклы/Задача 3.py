print()  # IQ
print("Задача №3.\nВыберите способ реализации задачи.\nДля этого введите цифру выбранного цикла:\n1. while\n2. for")
print()

sel_numb = int(input())
print()

print("Введите целое количество тестируемых людей:", end=' ')
n = int(input())
print("Укажите для", n, "людей их IQ:")
if sel_numb == 1:
    iq = int(input('1: '))
    print(0)
    i = 1
    s = iq
    while i < n:
        avr = s / i
        iq = int(input(str(i + 1) + ': '))
        if iq > avr:
            print('>', sep='\n')
        elif iq < avr:
            print('<')
        else:
            print(0)
        i += 1
        s += iq
elif sel_numb == 2:
    iq = int(input('1: '))
    print(0)
    i = 1
    s = iq
    for i in range(1, n):
        avr = s / i
        iq = int(input(str(i + 1) + ': '))
        if iq > avr:
            print('>', sep='\n')
        elif iq < avr:
            print('<')
        else:
            print(0)
        s += iq
else:
    input("Ошибка! Неверный ввод.")
