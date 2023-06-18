from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



#//----------// Snek's Menu //----------//
def Window():
    class Launcher(QMainWindow):

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Snek launcher")
            self.setGeometry(400, 200, 500, 550)
            self.UiComponents()
            self.show()


        def UiComponents(self):
        #//----------// Window //----------//

            self.label = QLabel(self)


        #//----------// Buttons //----------//

            button0 = QPushButton("Hello Player", self)
            button0.setFont(QFont('Comic Sans MS', 50))
            button0.setStyleSheet("background-color: cornsilk; color: yellowgreen")
            button0.setGeometry(-5, 0, 510, 200)

            button1 = QPushButton("Play Snek", self)
            button1.setFont(QFont('Comic Sans MS', 30))
            button1.setStyleSheet("background-color: cornsilk; color: indigo")
            button1.setGeometry(-5, 190, 510, 90
                                )
            button2 = QPushButton("Watch AI playing Snek", self)
            button2.setFont(QFont('Comic Sans MS', 18))
            button2.setStyleSheet("background-color: cornsilk; color: lightslategrey")
            button2.setGeometry(-5, 280, 510, 90)

            button3 = QPushButton("Player's score history", self)
            button3.setFont(QFont('Comic Sans MS', 18))
            button3.setStyleSheet("background-color: cornsilk; color: hotpink")
            button3.setGeometry(-5, 370, 510, 90)

            button4 = QPushButton("Exit", self)
            button4.setFont(QFont('Comic Sans MS', 18))
            button4.setStyleSheet("background-color: cornsilk; color: crimson")
            button4.setGeometry(-5, 460, 510, 90)


        #//-----// Defining Action of Buttons //-----//

            button0.clicked.connect(self.surprise)
            button1.clicked.connect(self.play)
            button2.clicked.connect(self.watch)
            button3.clicked.connect(self.points)
            button4.clicked.connect(self.end)

        def surprise(self):
            print("Wonsz zeczny jest niebezbieczny!")
            wonsz = open("111.txt", "r")
            wonsz1 = wonsz.readlines()
            for x in wonsz1:
                print(x[:-2])
            wonsz.close()
            
        def play(self):
            game.gameLoop('h')

        def watch(self):
            game.gameLoop('a')

        def points(self):
            tabela = open("wyniki.txt", "r")
            tabela1 = tabela.readlines()
            print("Player's scores")
            for x in tabela1:
                print(x.strip('\n'))
            tabela.close()

        def end(self):
            game.gameLoop('q')


    App1 = QApplication(sys.argv)
    window = Launcher()
    App1.exec()

import game

#wywołanie launchera gry
Window()



###############################################
#                 WYMAGANIA                   #
###############################################
# [X] Podział na projektu na moduły           # Wszyscy
#                                             #
# [X] Adnotacje do metod i funkcji            # Wszyscy
#                                             #
# [X] Paradygmat obiektowy                    # Wszyscy
#                                             #
# [X] Biblioteki wspomagające obliczenia inż  # Bartek
#                                             #
# [X] Operacje na plikach                     # Mikołaj + Kuba
#                                             #
# [X] GUI wykorzystujące qtframework          # Mikołaj + Kuba
#                                             #
###############################################



###############################################
#                DO ZROBIENIA                 #
###############################################
# [X] Cykl Hamiltona                          # Bartek + Mikołaj
#     (X) Statyczny                           #
#     (X) Losowy                              #
#                                             #
# [X] Funkcja skracająca cykl Hamiltona       # Wszyscy
#                                             #
# [X] Adnotacje do metod i funkcji            # Wszyscy
#                                             #
# [X] Wykrywanie wygrwanej                    # Wszyscy
#                                             #
# [X] Operacje na plikach                     # Wszyscy
#                                             #
# [X] GUI wykorzystujące qtframework:         # Mikołaj + Kuba
#     (X) Dedykowane pole na grę              #
#     (X) Wybór pomiędzy gracz/AI             #
#     (X) Ogólna estetyka                     #
#                                             #
###############################################
