from defslovar import *
from string import ascii_letters

alphabet_l = "йцукенгшщзхъфывапролджэячсмитьбю"
alphabet_u = alphabet_l.upper()
alphabet = alphabet_l + alphabet_u
alphabet1 = list(alphabet)
betabet_l = "qwertyuiopasdfghjklzxcvbnm"
betabet_u = betabet_l.upper()
betabet = betabet_l + betabet_u
betabet1 = list(betabet)
rus = []
engl = []
rus = loe_fail("rus.txt")
engl = loe_fail("engl.txt")
while True:
    v = int(
        input(
            "1.Перевести \n2.Добавить слово \n3.Изменить слово \n4.Проверить знания \n5.Выход "
        )
    )
    if v == 1:  # TRANSLATE
        translate1(rus, engl)
    elif v == 2:  # ADD
        text = input("Введи слово: ")
        text1 = list(text)
        if text1[0] in betabet1:
            kirjuta_fail("eng.txt", text)
            text = input("Введите слово на русском: ")
            kirjuta_fail("rus.txt", text)
        elif text1[0] in alphabet1:
            kirjuta_fail("rus.txt", text)
            text = input("Введите слово на английском: ")
            kirjuta_fail("engl.txt", text)
    elif v == 3:  # EDIT
        edit2("engl.txt", "rus.txt", engl, rus)
        # recreate(rus, engl)М
    elif v == 4:
        znanie(rus, engl)
    elif v == 5:
        break

# t=int(input("Кол-во раз"))
# for j in range(t):
