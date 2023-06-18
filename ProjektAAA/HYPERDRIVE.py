import hamilton as h

#funkcja skracająca drogę w cyklu w przypadku wykrycia "lepszego" ruchu (na podstawie odległości od jabłka mierzonej w liczbie...
#pól w cyklu pozostałych między głową węża a jabłkiem)
def speed(glowa,dupa,jablko,cc,tab,rozmiar_plansza,rozmiar_waz):
    do_jablka, oryginalny_ruch = h.gps(glowa,jablko, tab)

    #wygenerowanie 4 potencjalnych ruchów na podstawie współrzędnych gowy
    x, y =  glowa[0], glowa[1]
    gora, prawo, lewo, dol = (x,y+1),(x+1,y),(x-1,y),(x,y-1)    
    lista_kierunku = list((gora, prawo, lewo, dol))
    
    #wykluczenie z szukania skrótu ruchów samobójczych
    if gora[0] < 0 or gora[1] < 0 or gora[0] >= rozmiar_plansza[0] or gora[1] >= rozmiar_plansza[1]:
        lista_kierunku.remove(gora)
    if prawo[0] < 0 or prawo[1] < 0 or prawo[0] >= rozmiar_plansza[0] or prawo[1] >= rozmiar_plansza[1]:
        lista_kierunku.remove(prawo)
    if lewo[0] < 0 or lewo[1] < 0 or lewo[0] >= rozmiar_plansza[0] or lewo[1] >= rozmiar_plansza[1]:
        lista_kierunku.remove(lewo)
    if dol[0] < 0 or dol[1] < 0 or dol[0] >= rozmiar_plansza[0] or dol[1] >= rozmiar_plansza[1]:
        lista_kierunku.remove(dol)

    #wykluczenie z listy ruchów alternatywnych ruchu podstawowego oraz ruchu poprzedniego (segmentu węża zaraz za głową)
    for i in lista_kierunku:
        if oryginalny_ruch == i:
            lista_kierunku.remove(i)
        if dupa == i:
            lista_kierunku.remove(i)

    #porównanie ruchu oryginalnego z ruchem alternatywnym (czy opłaca się skracać)
    #w przypadku wykrycia alternatywnego ruchu skracającego drogę - zastąpienie ruchu oryginalnego alternatywnym
    for i in lista_kierunku:
       alt_odleglosci, alt_ruch = h.gps(i,jablko,tab)
       if alt_odleglosci < do_jablka and alt_odleglosci >= rozmiar_waz:
           oryginalny_ruch = i
           do_jablka = alt_odleglosci


    print('HYP: ', oryginalny_ruch, do_jablka )
    return oryginalny_ruch