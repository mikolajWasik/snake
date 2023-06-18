import random

#ten moduł jest trudny do opisu słownego więc do projektu dołączamy rysunek wyjaśniający pod nazwą "schemat_Prims.png"

#wygenerowanie losowego cyklu Hamiltona na podstawie obrysu drzew MST na siatce punktów dwukrotnie rzadszej niż siatka docelowedo cyklu
def prims_gen( board_width, board_height ):
    
    prims_board_width = board_width / 2
    prims_board_height = board_height / 2
    
    #//----------// GENERATING LIST OF LAYERS //----------//
    #wygenerowanie siatki dwukronie rzadszej
    layer = []
    layers = []
    prims_x = 0
    prims_y = 0
    while 1:
        while 1:
            if prims_x >= prims_board_width:
                break
            else:
                layer.append((prims_x,prims_y))
            prims_x += 1
        prims_y += 1
        prims_x = 0
        layers.append(layer)
        layer = []
        if prims_y >= prims_board_height:
            break



    #//----------// GENERATING LIST OF CONNECTED LAYERS //----------//
    #zaktualizowanie siatki dwukrotnie rzadszej o informacje o położeniu połączenia między warstwami
    con_layers = []
    con_layer = []
    layer_iter = 0
    prev_layer_iter = 0
    connection = random.randint(0,prims_board_width - 1)
    prev_connection = 0

    for layer in layers:
        for element_of_layer in layer:
            if prev_layer_iter == prev_connection and layer != layers[0]:
                if prev_connection == connection:
                    con_layer.append((element_of_layer,'bb'))
                else:
                    if layer == layers[-1]:
                        con_layer.append((element_of_layer,'uu'))
                    elif connection > prev_connection:
                        con_layer.append((element_of_layer,'ru'))
                    else:
                        con_layer.append((element_of_layer,'lu'))
            elif layer_iter == connection and layer != layers[-1]:
                if layer == layers[0]:
                    con_layer.append((element_of_layer,'dd'))                
                elif connection > prev_connection:
                    con_layer.append((element_of_layer,'ld'))
                else:
                    con_layer.append((element_of_layer,'rd'))
            else:
                con_layer.append((element_of_layer,'  '))
            layer_iter += 1
            prev_layer_iter += 1
        layer_iter = 0
        prev_layer_iter = 0
        con_layers.append(con_layer)
        con_layer = []
        prev_connection = connection
        connection = random.randint(0,prims_board_width - 1)

    #wywołanie funkcji interpreter (jej dokładniejsy opis ponieżej)
    hamilton = prims_interpreter(con_layers)

    return hamilton



#wygenerowanie cyklu Hamiltona na siatce dwukrotnie gęstszej niż stworzona wcześniej siatka punktów (wykorzystywana wyżej)
def prims_interpreter(con_layers):
    hamilton_up = []
    hamilton_down = []
    hamilton_raw = []
    hamilton_up_front = []
    hamilton_up_back = []
    hamilton_down_front = []
    hamilton_down_back = []
    hamilton_cycle = [(0,0)]
    beg = True
    up_flag = False
    down_flag = False

    #krok pośredni potrzebny do wygenerowania siatki dwukrotnie gęstszej (wstawianie do listy znaku...
    #rozdzielającego - potrzebne w kroku drugim)
    for con_layer in con_layers:
        for element_of_con_layer in con_layer:
            prims_element = element_of_con_layer[0]
            layer_connection = element_of_con_layer[1]
            #wygenerowanie punktów siatki dwukrotnie większej (dokładniejszy opis przy definicji)
            left_up, right_up, left_down, right_down = prims_return_satelite(prims_element)
            
            hamilton_up.append(left_up)
            if layer_connection == 'uu' or layer_connection == 'ru' or layer_connection == 'lu' or layer_connection == 'bb':
                hamilton_up.append('b')
            hamilton_up.append(right_up)

            hamilton_down.append(left_down)
            if layer_connection == 'dd' or layer_connection == 'rd' or layer_connection == 'ld' or layer_connection == 'bb':
                hamilton_down.append('b')
            hamilton_down.append(right_down)

        hamilton_raw.append((hamilton_up,hamilton_down))
        hamilton_up = []
        hamilton_down = []

    #drugi krok pośredni (rozdzielenie listy punktów warstwy na dwie osobne listy - przed i za połączeniem)
    for layer_raw in hamilton_raw:
        for up_iter in layer_raw[0]:
            if up_iter == 'b':
                up_flag = True
                continue
            if up_flag:
                hamilton_up_back.append(up_iter)
            else:
                hamilton_up_front.append(up_iter)
        hamilton_up.append((hamilton_up_front,hamilton_up_back))
        hamilton_up_back = []
        hamilton_up_front = []
        up_flag = False

        for down_iter in layer_raw[1]:
            if down_iter == 'b':
                down_flag = True
                continue
            if down_flag:
                hamilton_down_back.append(down_iter)
            else:
                hamilton_down_front.append(down_iter)
        hamilton_down.append((hamilton_down_front,hamilton_down_back))
        hamilton_down_back = []
        hamilton_down_front = []
        down_flag = False
    
    back = []
    beg = True

    #wygenerowanie niepełnego cyklu Hamiltona obrysowującego, utworzone z połączenia...
    #poszczególnych warstw, drzewo MST (pierwszej połowy)
    for down, up in zip(hamilton_down,hamilton_up):
        if beg:
            back = up[0]
            back.reverse()
            del back[-1]
            beg = False
        else:
            upp = up[0]
            upp.reverse()
            hamilton_cycle.extend(upp)            
        hamilton_cycle.extend(down[0])
        
    beg = True
    hamilton_down.reverse()
    hamilton_up.reverse()
    #wygenerowanie reszty cyklu (drugiej połowy)
    for down, up in zip(hamilton_down, hamilton_up):
        if beg:
            beg = False
        else:
            hamilton_cycle.extend(down[1])
        upp = up[1]
        upp.reverse()
        hamilton_cycle.extend(upp)

    hamilton_cycle.extend(back)

    return hamilton_cycle



#wygenerowanie punktów siatki dwukrotnie gęstszej na podstawie danego punktu z siatki rzadszej (w tym przypadku punkt siatki...
#rzadszej jest w centrum kwadratu utowrzonego przez 4 najblizsze sobie punkty siatki gęstszej)
def prims_return_satelite(prims_point):
    x_point = prims_point[0]
    y_point = prims_point[1]

    left_up = (x_point*2,y_point*2)
    right_up = (x_point*2 + 1, y_point*2)
    left_down = (x_point*2,y_point*2 + 1)
    right_down = (x_point*2 + 1, y_point*2 + 1 )


    return left_up, right_up, left_down, right_down