import pygame
import time
import random
import sys
import hamilton
import HYPERDRIVE
import interpreter
import Prims
import math


pygame.init()

#zestaw kolorów wykorzystywanych w grze
white = ( 255, 255, 255 )
yellow = ( 255, 255, 102 )
black = ( 0, 255, 0 )
red = ( 50, 153, 213 )
green = ( 255, 10, 10 )
blue = ( 0, 0, 0 )

#definicja rozmiaru planszy w pikselach
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode( (600, 400) )
pygame.display.set_caption( 'Projekt AAA' )

clock = pygame.time.Clock()

#rozmiar segmentu węża i częstotliwość odświeżania gry
snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont( "bahnschrift", 25 )
score_font = pygame.font.SysFont( "comicsansms", 35 )

#funkcja wyświetlająca punkty na bieżąco podczas grania
def Your_score(score):
    value = score_font.render( "Your Score: " + str(score), True, yellow )
    dis.blit(value, [0, 0])


#funkcja opisująca budowę węża
def our_snake( snake_block, snake_list ):
    for x in snake_list:
        pygame.draw.rect( dis, black, [x[0], x[1], snake_block, snake_block] )


#definicja funkcji wyświetlającej komunikat po zakończeniu gry 
def message( msg, color ):
    mesg = font_style.render( msg, True, color )
    dis.blit( mesg, [dis_width / 6, dis_height / 3] )


#główny kod gry
def gameLoop(player):
    if player == 'q':
        game_over = True
        pygame.quit()
        quit()
    game_over = False
    game_close = False
    first_move = True

    #startowa pozycja węża
    x1 = 0
    y1 = 0
    
    #zmienne odpowiedzialne za kierunek poruszania się węża
    x1_change = 0
    y1_change = 0

    #rozmiar planszy w polach (1 pole = 10*10 pikseli)
    x1_board_h = dis_width / 10
    y1_board_h = dis_height / 10
    board_h = ( x1_board_h, y1_board_h )

    #rozmiar planszy dwukrotnie zmniejszony (potrzebny do modułu "Prims.py")
    x1_h = x1_board_h / 2
    y1_h = y1_board_h / 2
    snake_head_h = ( 0, 0 )
    snake_tail_h = ( 0, 0 )
    #pozycja celu (wąż dąży do elementu n przed jabłkiem gdzie n = długość węża)
    goal = ( 0, 0 )


    #generowanie losowego cyklu Hamiltona (więcej o tym w module "Prims.py")
    hamilton_path = Prims.prims_gen( x1_board_h, y1_board_h )
    print(hamilton_path)
    snake_List = []
    length_of_snake = 1

    #losowo generowane współrzędne pierwszego jabłka
    foodx = round( random.randrange(0, dis_width - snake_block ) / 10.0 ) * 10.0
    foody = round( random.randrange(0, dis_height - snake_block ) / 10.0 ) * 10.0

    foodx_h = foodx / 10
    foody_h = foody / 10 
    food_h = ( foodx_h , foody_h )

    #pętla główna gry
    while not game_over:

        if length_of_snake >= 2400:
            game_close = True
        #akcja w przypadku wygranej/przegranej
        if game_close:
            dis.fill( blue )
            if length_of_snake < 2400:
                message( "You Lost!", red )
            else:
                message( "You Won!", red )
            if player == 'h':
                wyniki = open("wyniki.txt", "a")
                wyniki.write(str(length_of_snake - 1) + "\n")
                wyniki.close()
            Your_score( length_of_snake - 1 )
            pygame.display.update()
            break


        #sekcja sterowania dla gracza
        #//----------// HUMUS //----------//
        if player == 'h':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
        #//----------// HUMUS //----------//


        #sekcja sterowania dla bota (algorytmu)
        #//----------// AI //----------//
        if player == 'a':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            goal = HYPERDRIVE.speed(snake_head_h, snake_tail_h, food_h, 0, hamilton_path, board_h, length_of_snake)
            print('GOAL: ',goal)
            direction = interpreter.translator(snake_head_h, goal)
            print('\n')
            if direction == 'left':
                snake_tail_h = snake_head_h
                snake_head_h = ( snake_tail_h[0] - 1, snake_tail_h[1] )
                x1_change = -snake_block
                y1_change = 0
            elif direction == 'right':
                snake_tail_h = snake_head_h
                snake_head_h = ( snake_tail_h[0] + 1, snake_tail_h[1] )
                x1_change = snake_block
                y1_change = 0
            elif direction == 'up':
                snake_tail_h = snake_head_h
                snake_head_h = ( snake_tail_h[0], snake_tail_h[1] - 1 )
                y1_change = -snake_block
                x1_change = 0
            elif direction == 'down':
                snake_tail_h = snake_head_h
                snake_head_h = ( snake_tail_h[0], snake_tail_h[1] + 1 )
                y1_change = snake_block
                x1_change = 0
        #//----------// AI //----------//


        #aktualizowanie położenia węża i wyświetlania
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill( blue )
        pygame.draw.rect( dis, green, [foodx, foody, snake_block, snake_block] )
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len( snake_List ) > length_of_snake:
            del snake_List[0]
        #wykrycie kolizji głowy węża z samym sobą
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake( snake_block, snake_List )
        Your_score( length_of_snake - 1 )

        pygame.display.update()
        #sprawdzenie czy wąż zjadł jabłko, zwiększenie rozmiaru węża i losowanie współrzędnych kolejnych jabłek
        if x1 == foodx and y1 == foody:
            foodx = round( random.randrange( 0, dis_width - snake_block ) / 10.0 ) * 10.0
            foody = round( random.randrange( 0, dis_height - snake_block ) / 10.0 ) * 10.0
            foodx_h = foodx / 10
            foody_h = foody / 10
            food_h = ( foodx_h , foody_h )
            length_of_snake += math.floor(math.pow(1, 1))

        clock.tick( snake_speed )
