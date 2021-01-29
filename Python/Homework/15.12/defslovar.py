import random as r


def loe_fail(f):
    fail = open(f, "r", encoding="utf-8-sig")
    mas = []
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas


def kirjuta_fail(f, rida):
    fail = open(f, "a", encoding="utf-8-sig")
    fail.write(rida + "\n")  # Сохранит значение в файл
    fail.close()


def translate1(s1, s2):
    text = input("text:")
    if text in s1:
        print(f"{text}-{s2[s1.index(text)]}")
    elif text in s2:
        print(f"{text}-{s1[s2.index(text)]}")
    else:
        print(f"{text} puudub")


def add1(f1, f2, rus, engl):
    with open(f1, "a", encoding="utf-8-sig") as f1:
        f1.write(rus + "\n")
    with open(f2, "a", encoding="utf-8-sig") as f2:
        f2.write(engl + "\n")


def edit1(s1, s2):
    text = input("Введите слово, которое вы хотите изменить :")
    if text in s1:
        return text
    return s1.replace({s2[s1.index(text)]}, text)  # что заменить -  на что


def edit2(l1, l2, l3, l4):  # Функция для поиска файла и последующей его замены
    word = input("Введите слово которое хотите найти : ")
    if word in l3:
        print(f"{word}")
        with open(l1, encoding="utf-8-sig") as file_in:
            text = file_in.read()  # Открытие файла и копирование файла в буфер
        n_word = input("Введи новое слово => ")
        text = text.replace(word, n_word)  # Замена существуещего слова на новое
        with open(l1, "w", encoding="utf-8-sig") as file_out:
            file_out.write(text)  # Очистка файла и запись из буфера + изменённое слово
    elif word in l4:
        print(f"{word}")
        with open(l2, encoding="utf-8-sig") as file_in:
            text = file_in.read()
        n_word = input("Введи новое слово : ")
        text = text.replace(word, n_word)
        with open(l2, "w", encoding="utf-8-sig") as file_out:
            file_out.write(text)


# def edit3(s1, s2):
#    text = input("Введите слово: ")
#    if text in s1:
#        print(f"{text}-{s2[s1.index(text)]}")
#    elif text in s2:
#        print(f"{text}-{s1[s2.index(text)]}")
#    else:
#        print(f"{text} такого слова нет")
#    text = int(input("Слово корректное ? \n1.Да \n2.Нет"))
#    if text == 1:
#        continue
#    elif text == 2:
#        text = int(input("Хотите изменить ? \n1.Да \n2.Нет"))
#        if text == 1:
#            pass
#        elif text == 2:
#            break


def znanie(f1, f2):
    t = int(input("Вберите язык\n1-Русский\n2-Английский : "))
    if t == 1:
        kol = int(input("Сколько слов вы хотите перевести? : "))
        koll = kol
        bal = 0
        while kol > 0:
            try:
                r1 = r.choice(f1)
                print(r1, "\n")
                ii = f1.index(r1)
                slovo = input("Введите перевод слова : ")
                ii2 = f2.index(slovo)
                if ii == ii2:
                    print(f"Правильно")
                    bal += 1
                    kol -= 1
                else:
                    print(f"Неправильно")
                    kol -= 1
            except:
                TypeError
        print("Вы ответили на", "{:.0%}".format(bal / koll), "правильно")
    if t == 2:
        kol = int(input("Сколько слов вы хотите перевести? : "))
        koll = kol
        bal = 0
        while kol > 0:
            try:
                r2 = r.choice(f2)
                print(r2, "\n")
                ii = f2.index(r2)
                slovo = input("Введите перевод слова : ")
                ii2 = f1.index(slovo)
                if ii == ii2:
                    print(f"Правильно")
                    bal += 1
                    kol -= 1
                else:
                    print(f"Неправильно")
                    kol -= 1
            except:
                TypeError
        print("Вы ответили на", "{:.0%}".format(bal / koll), "правильно")
