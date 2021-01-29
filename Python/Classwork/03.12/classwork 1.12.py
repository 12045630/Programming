from defClass import *

pa = [4000, 500, 999, 555, 2500]
ini = ["A", "B", "A", "D", "E"]

while 1:
    print(
        "0.Выход \n1.Добавление \n2.Удаление  \n3.Максимальная зп\n4.Минимальная зп \n5.Сортировка \n6.Одинаковые зп \n7.Поиск зп по имени \n8.Больше/меньше указанной суммы \n9.Toп 3 по зп \n10.Средняя зп \n11.Зп с учётом подоходного налога "
    )
    v = int(input("=> "))
    if v == 0:
        break
    elif v == 1:
        kogus = int(input("Kogus => "))
        lisamine(pa, ini, kogus)
    elif v == 2:
        ini, pa = kustutamine(pa, ini)
        print(ini, pa)
    elif v == 3:
        suurimpalk(pa, ini)
    elif v == 4:
        vaiksempalk(pa, ini)
    elif v == 5:
        sort_list(pa, ini)
    elif v == 6:
        odinakov(pa, ini)
    elif v == 7:
        palk_nini_jargi(pa, ini)
    elif v == 8:
        bolwe_menwe(pa, ini)
    elif v == 9:
        Top3(pa, ini)
    elif v == 10:
        keskmine(pa, ini)
    elif v == 11:
        tulumaks(pa, ini)