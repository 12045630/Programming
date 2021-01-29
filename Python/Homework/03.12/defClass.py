def lisamine(p, i, a):
    for j in range(a):
        i.append(input("Sisesta nimi => "))
        p.append(input("Sisesta palk => "))
    print(i, p)


def kustutamine(p, i):
    n = input("Nimi => ")
    co = i.count(n)
    t = 0
    if co > 1:
        for j in range(co):
            ind = i.index(n, t)
            print(f"{ind}, {n}")
            t = ind + 1
        ind = int(input("keda kustutame ära? => "))
        i.pop(ind)
        p.pop(ind)
    return i, p


def suurimpalk(p, i):
    suurim = max(p)
    k = p.count(suurim)
    t = 0
    if k > 1:
        print(f"Suurim palk on {suurim} järgmistel inimestel")
        for j in range(k):
            ind = p.index(suurim, t)
            print(f"{i[ind]}")
            t = ind + 1
    else:
        print("Inimise nimi on", i[p.index(suurim)], "tema palk on ", suurim)


def vaiksempalk(p, i):
    vaike = min(p)
    k = p.count(vaike)
    t = 0
    if k > 1:
        print(f"Väiksem palk on {vaike} järgmistel inimestel")
        for j in range(k):
            ind = p.index(vaike, t)
            print(f"{i[ind]}")
            t = ind + 1
    else:
        print("Inimise nimi on", i[p.index(vaike)], "tema palk on ", vaike)


def suurvaike(p, i):
    a = input("Vali funktsion -max/min")
    suurim_vaiksem = eval(str(a) + str("(") + str(p) + str(")"))  # max(p) min(p)
    if a == "max":
        mida = "Suurim"
    else:
        mida = "Vaiksem"
    k = p.count(suurim_vaiksem)
    t = 0
    if k > 1:
        print(f"{mida} palk on {suurim_vaiksem} järgmistel inimestel: ")
        for j in range(k):
            ind = p.index(suurim_vaiksem)
            print(f"{i[ind]}")
            t = ind + 1
    else:
        print(
            "Inimese nimi on ",
            i[p.index(suurim_vaiksem)],
            "tema palk on",
            suurim_vaiksem,
        )


def sort_list(p, i):
    a = int(input("Сортировака 1 - по возростанию, 2 - по убыванию => "))
    if a == 1:
        sort_list_voz(p, i)
    else:
        sort_list_ub(p, i)


def sort_list_voz(p, i):
    for y in range(0, len(p)):
        for x in range(0, len(p)):
            if p[y] > p[x]:
                abi = p[y]
                p[y] = p[x]
                p[x] = abi
                ##########
                abi = i[y]
                i[y] = i[x]
                i[x] = abi
    t = 0
    for palk in p:
        print(palk, i[t])
        t += 1


def sort_list_ub(p, i):
    for y in range(0, len(p)):
        for x in range(0, len(p)):
            if p[y] < p[x]:
                abi = p[y]
                p[y] = p[x]
                p[x] = abi
                ##########
                abi = i[y]
                i[y] = i[x]
                i[x] = abi
    t = 0
    for palk in p:
        print(palk, i[t])
        t += 1


def odinakov(p, i):
    t = 0
    p1 = []
    i1 = []
    for j in p:
        if p.count(j) > 1:
            for n in p:
                if j == n:
                    print(f"{i[t]} saab kätte {j}")
                    p1.append(j)
                    i1.append(i[t])
                    break
        t += 1
    sort_list(p1, i1)


def palk_nini_jargi(p, i):
    a = input("Введите имя => ")
    k = i.count(a)
    t = 0
    if k > 1:
        print(f"{a}")
        for j in range(k):
            ind = i.index(a, t)
            print(f"{a} = {p[ind]}")
            t += 1
    elif k == 1:
        print(f"Inimise nimi on {a} tema palk on {p[i.index(a)]}")
    else:
        print("Человека нет")


def bolwe_menwe(p, i):
    piir = int(input("Введите зарплату => "))
    a = input("< или >")
    t = 0
    for palk in p:
        if eval(str(palk) + a + str(piir)):
            ind = p.index(palk, t)
            print(f"{palk} saab katte {i[ind]}")
            t += 1


def Top3(p, i):
    while 1:
        o = int(input("Ваш выбор \n1. Топ 3 (MIN-MAX или  \n 2.Топ 3 (MAX-MIN) "))
        if o == 1:
            for y in range(0, len(p)):  # len - кол-во
                for x in range(0, len(p)):
                    if p[y] < p[x]:
                        abi = p[y]
                        p[y] = p[x]
                        p[x] = abi

                        abi = i[y]
                        i[y] = i[x]
                        i[x] = abi
            print(p[0], i[0])
            print(p[1], i[1])
            print(p[2], i[2])
            break
        elif o == 2:
            for y in range(0, len(p)):
                for x in range(0, len(p)):
                    if p[y] > p[x]:
                        abi = p[y]
                        p[y] = p[x]
                        p[x] = abi

                        abi = i[y]
                        i[y] = i[x]
                        i[x] = abi
            print(p[0], i[0])
            print(p[1], i[1])
            print(p[2], i[2])
            break


def keskmine(p, i):
    for y in range(0, len(p)):
        for x in range(0, len(p)):
            if p[y] < p[x]:
                abi = p[y]
                p[y] = p[x]
                p[x] = abi

                abi = i[y]
                i[y] = i[x]
                i[x] = abi
    c = len(p)
    print(f"Всего пользователей: {c}")
    k = c // 2
    if c % 2 == 0:
        print(p[k - 1], i[k - 1])
        print(p[k], i[k])
    else:
        print(p[k], i[k])


def tulumaks(p, i):
    c = len(p)
    c = c - 1
    while c != -1:
        if 500 < p[c] <= 1200:
            k = (p[c] - 500) * 0.8
            print(i[c], "-", k)
        elif p[c] <= 500:
            print(i[c], "-", p[c])
        elif 1200 < p[c] < 2100:
            k = (p[c] - (500 - ((p[c] - 1200) * 0.55556))) * 0.8
            print(i[c], "-", k)
        elif 2100 <= p[c]:
            k = p[c] * 0.8
            print(i[c], "-", k)
        c = c - 1
