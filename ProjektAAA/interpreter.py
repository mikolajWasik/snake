#przetłumaczenie współrzędnych następnego, względem głowy, kroku cyklu Hamiltona na kierunek ruchu
def translator(head, goal):
    direction = 'up'

    print('TRAN: ',head, goal)

    if head[0] == goal[0]:
        if goal[1] > head[1]:
            direction = 'down'
        else:
            direction = 'up'
    if head[1] == goal[1]:
        if goal[0] > head[0]:
            direction = 'right'
        else:
            direction = 'left'
    print('DIR: ',direction)
    return direction