print()  # Последовательность Коллатца
print("Задача №6.\n")  # Задача на while

print("Введите целое число:", end=' ')
n = int(input())
steps = 0

flag = False  # Флаг для входа единицы в цикл
if n == 1:
    n += 1
    flag = True

while n != 1:
    if flag:  # Условие для входа единицы в цикл
        n -= 1
        flag = False
    if n % 2 == 0:
        n = n / 2
        steps += 1
    else:
        n = 3 * n + 1
        steps += 1
print("Требуемое количество шагов последовательности:", steps)
