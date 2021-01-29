def Autopassword(pw):
    import random

    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    pw1 = "".join([random.choice(ls) for x in range(12)])
    pw.append(pw1)
    print(f"Ваш пароль - {pw1}")


def ManualPassword(pw):
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper()
    st0 = list(str0)
    st1 = list(str1)
    st2 = list(str2)
    st3 = list(str3)
    print(
        "Пароль должен содержать цифры, буквы в нижнем и верхнем регистре, спец. символы."
    )
    while True:
        pw1 = input("Придумайте пароль - ")
        pw_list = list(pw1)
        if list(set(pw_list) & set(st0)):
            if list(set(pw_list) & set(st1)):
                if list(set(pw_list) & set(st2)):
                    if list(set(pw_list) & set(st3)):
                        print(f"Ваш пароль {pw1}")
                        pw.append(pw1)
                    else:
                        print("Пароль должен содержать буквы верхнего регистра.")
                        continue
                else:
                    print("Пароль должен содержать буквы нижнего регистра.")
                    continue
            else:
                print("Пароль должен содержать цифры. ")
                continue
        else:
            print("Пароль должен содержать спец. символы.")
            continue
        break


# def TryTry():
#    answ2 = input("Введите ваш логин ")
#    print("У вас будет 3 попытки, чтобы вспомнить свои данные. ")
#    while answ3 not in pw:
#        try:
#            tru = 3
#            while tru <= 3 and tru >= 1:
#                try:
#                    answ3 = input("Введите ваш пароль ещё раз ")
#                    if answ3 in pw:
#                        print(f"Добо пожаловать - {answ2}")
#                        break
#                    else:
#                        tru = tru - 1
#                        print(f"Неправильно, у вас {tru} попыток !")
#                        if tru == 0:
#                            print("К сожалению, у вас закончились попытки.")
#                            break
#                except:
#                    TypeError
#            break
#        except:
#            TypeError


def Login(lg, pw):
    answ2 = input("Введите ваш логин ")
    if answ2 in lg:
        answ3 = input("Введите ваш пароль ")
        if answ3 in pw:
            print(f"Добро пожаловать - {answ2}")
        else:
            print(
                "Вы ввели неправильный пароль. У вас есть 3 попытки, чтобы вспомнить "
            )
            while answ3 not in pw:
                try:
                    tru = 3
                    while tru <= 3 and tru >= 1:
                        try:
                            answ3 = input("Введите ваш пароль ещё раз ")
                            if answ3 in pw:
                                print(f"Добо пожаловать - {answ2}")
                                break
                            else:
                                tru = tru - 1
                                print(f"Неправильно, у вас {tru} попыток !")
                                if tru == 0:
                                    print("К сожалению, у вас закончились попытки.")
                                    break
                        except:
                            TypeError
                    break
                except:
                    TypeError
    else:
        print("Вы ввели неправильный логин или же его не существует. ")
        vopr = int(input("\n 1. Попробовать ещё раз \n 2. Регистрация "))
        if vopr == 1:
            print("У вас будет 3 попытки, чтобы вспомнить свой логин. ")
            while answ2 not in lg:
                try:
                    tru = 3
                    while tru <= 3 and tru >= 1:
                        try:
                            answ2 = input("Введите логин ещё раз  ")
                            if answ2 in lg:
                                pw1 = input("Введите ваш пароль ")
                                if pw1 in pw:
                                    print(f"Добо пожаловать - {answ2}")
                                    break
                                else:
                                    print("К сожалению, пароль неправильый. ")
                            else:
                                tru = tru - 1
                                print(f"Неправильно, у вас {tru} попыток !")
                                if tru == 0:
                                    print("К сожалению, у вас закончились попытки.")
                                    break
                        except:
                            TypeError
                    break
                except:
                    TypeError


def registr(lg, pw):
    lg.append(input("Придумайте логин - "))
    answ2 = int(
        input(
            "Выберите дальнейшее действие \n 1. Автомотическое создание пароля \n 2. Самостоятельное создание пароля "
        )
    )
    if answ2 == 1:
        Autopassword(pw)
    elif answ2 == 2:
        ManualPassword(pw)