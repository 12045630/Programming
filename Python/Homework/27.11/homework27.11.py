import random
from defHOME import *

lg = ["vad", "vadim"]
pw = ["vadd"]
tru = 4
print(
    "Добрый день. Добро пожаловать у нас на сайте. Выберите пожалуйста вариант дальнейших действий."
)
# После того ,как введёт логин и напишет, что такого нет - предложить создать новый.
# Переделать вход, без цикла. if answ in login:
# Попытаться реализовать ограниченнок кол-во ввода пароля.
while True:
    answ1 = int(input("\n 1. Авторизироваться  \n 2. Регистрация \n 3. Выход "))
    print(lg)
    print(pw)
    # Авторизация
    if answ1 == 1:
        Login(lg, pw)
    elif answ1 == 2:
        lg.append(input("Придумайте логин - "))
        answ2 = int(
            input(
                "Выберите дальнейшее действие \n 1. Автомотическое создание пароля \n 2. Самостоятельное создание пароля "
            )
        )
        if answ2 == 1:
            Autopassword(pw)
            answ3 = int(input("Желаете войти в систему ? \n 1. Да \n 2. Нет "))
            if answ3 == 1:
                answ2 = input("Введите ваш логин ")
                if answ2 in lg:
                    pw1 = input("Введите ваш пароль ")
                    if pw1 in pw:
                        print(f"Добро пожаловать {answ2}")
                    else:
                        print("Вы ввели неправильный пароль ")
                else:
                    print("Вы ввели неправильный логин ")
        elif answ2 == 2:
            ManualPassword(pw)
    elif answ1 == 3:
        break