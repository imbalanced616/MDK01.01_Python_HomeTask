import sys

print()  # Пароль
print("Задача №5.\n")  # Задача на while

print("Введите пароль:", end=' ')
password = input()
a = 0
while a == 0:
    if len(password) < 8:
        print("Короткий!")
        sys.exit()
    print("Введите пароль ещё раз:", end=' ')
    password_check = input()
    if password != password_check:
        print("Различаются.")
    elif "123" in password:
        print("Простой!")
    else:
        print("OK")
    a = 1

# Решение задачи без while

# print("Введите пароль:", end=' ')
# password = input()
# if len(password) < 8:
#    print("Короткий!")
#    sys.exit()
# print("Введите пароль ещё раз:", end=' ')
# password_check = input()
# if password != password_check:
#     print("Различаются.")
# elif "123" in password:
#     print("Простой!")
# else:
#     print("OK")
