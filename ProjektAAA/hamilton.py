#generowanie statycznego, z góry ustalonego cyklu Hamiltona
def generator(szerokosc, wysokosc):
    x = 0
    y = 0
    i = 1
    j = 0
    eject = 0

    lim_x = szerokosc
    lim_y = wysokosc

    #wygenerowany poniżej cykl ma kształ podobny do grzebienia, ale zrezygnowaliśmy z tego pomysłu na rzecz losowego cyklu...
    #ale szkoda było usuwać kod
    sciezka = [(x, y)]
    while 1:
        if (x == 0 or x % 2 == 0) and j != 1:
            if i < lim_y:
                y += 1
                a = (x, y)
                sciezka.append(a)
                i += 1
            else:
                x += 1
                i = 2
                a = (x, y)
                sciezka.append(a)
        elif x % 2 == 1 and j != 1:
            if i < lim_y:
                y -= 1
                a = (x, y)
                sciezka.append(a)
                i += 1
            else:
                if x != lim_x - 1:
                    i = 2
                    x += 1
                    a = (x, y)
                    sciezka.append(a)
                else:
                    i = 2
                    j = 1
        elif x == lim_x - 1 and y == 1:
            y -= 1
            i = 1
            a = (x, y)
            sciezka.append(a)
        elif i <= lim_x - 2:
            i += 1
            x -= 1
            a = (x, y)
            sciezka.append(a)         

        eject += 1
        if eject == lim_x * lim_y:
            break


    return(sciezka)


#tłumaczy wężowi jak poruszać się po stworzonej ściece (zwraca współrzędne kolejnego kroku w cyklu)
def gps(g, j, droga):
    i = 0
    odleglosc = 0
    kolejny = (0,0)
    koniec = droga[-1]
    
    a3 = True
    a2 = False
    a1 = False
    count = True
    found = False

    for i in droga:
        if i == g:
            if i == koniec:
                kolejny = droga[0]
            else:
                found = True
                continue
        if found:
            kolejny = i
            break


    for i in droga:
        if i == g:
            if a2:
                a3 = False
            a1 = True
            count = False
            if a2:
                count = True
        elif i == j:
            a2 = True
            count = False
            if a1:
                count = True
        elif count:
            odleglosc += 1

    if a3:
        odleglosc = len(droga) - odleglosc - 2

    return odleglosc, kolejny