print()  # Скидка
print("Задача №6.\n")  # Задача на while

print("Введите целое количество товаров:", end=' ')
n = int(input())
i = 1
prices = []
summa = 0
print("Введите цену за каждого товара:")
while i <= n:
    prices.append(float(input(str(i) + ': ')))
    if prices[i - 1] > 500:
        summa += prices[i - 1] - prices[i - 1] * 0.07  # Вычитаю 7% из цены товара, если он превышает 500 рублей
    else:
        summa += prices[i - 1]
    i += 1
print("Сумма товаров с учётом скидки:", summa, "рублей")
