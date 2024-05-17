# -*- coding: utf-8 -*-

import pygame, sys, fun

def main(screen, width, height, pzTrud, zpStat, los = False, gry = None):

    liczba_rzedow_i_kolumn = 6
    if los == False:
        gra_gracz = fun.Gra(screen, 50, 150, 301, 301, 0, liczba_rzedow_i_kolumn, pzTrud, los)
    else:
        gra_gracz = gry.zmien_opcje(screen, 50, 150, 301, 301, 0, liczba_rzedow_i_kolumn, pzTrud, los)
    gra_komputer = fun.Gra(screen, 450, 150, 301, 301, 1, liczba_rzedow_i_kolumn, pzTrud)

    przesuniecieX = gra_komputer.siatka.sX
    przesuniecieY = gra_komputer.siatka.sY
    wyborX = gra_komputer.siatka.x + przesuniecieX
    wyborY = gra_komputer.siatka.y + przesuniecieY
    wyborXpoczatek = wyborX
    wyborYpoczatek = wyborY
    X = 1
    Y = 1

    # 0 - gracz - start
    # 1 - gracz - pudło
    # 2 - gracz - trafiony
    # 3 - gracz - trafiony zatopiony
    # 4 - gracz - zły wybór
    # 5 - komputer - pudło
    # 6 - komputer - trafiony
    # 7 - komputer - trafiony zatopiony
    # 8 - komputer - start
    # -1 - koniec rozgrywki
    status_rozgrywki = 0

    while True:
        if (gra_gracz.liczba_niezniszczonych_statkow == 0) | (gra_komputer.liczba_niezniszczonych_statkow == 0):
            status_rozgrywki = -1
        
        if status_rozgrywki == 0:
            while True:
                if status_rozgrywki != 0:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10)

                font = pygame.font.Font(None, 75)
                text = font.render('Twój ruch', 1, 'gold')
                screen.blit(text, (275,25))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if wyborY > wyborYpoczatek:
                                wyborY -= przesuniecieY
                                Y -= 1
                        if event.key == pygame.K_DOWN:
                            if wyborY < wyborYpoczatek + (liczba_rzedow_i_kolumn - 1) * przesuniecieY:
                                wyborY += przesuniecieY
                                Y += 1
                        if event.key == pygame.K_LEFT:
                            if wyborX > wyborXpoczatek:
                                wyborX -= przesuniecieX
                                X -= 1
                        if event.key == pygame.K_RIGHT:
                            if wyborX < wyborXpoczatek + (liczba_rzedow_i_kolumn - 1) * przesuniecieX:
                                wyborX += przesuniecieX
                                X += 1
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = gra_komputer.ruch(Y, X)
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 1:
            while True:
                if status_rozgrywki != 1:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10, 'black')

                font = pygame.font.Font(None, 75)
                text = font.render('Twój ruch', 1, 'gold')
                screen.blit(text, (275,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (155,530))
                text = font.render('Pudło!', 1, 'white')
                screen.blit(text, (550,530))

                fun.rysuj_zaznaczenie(screen, 1*width/8, 530, 3*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 8
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 2:
            while True:
                if status_rozgrywki != 2:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10, 'black')

                font = pygame.font.Font(None, 75)
                text = font.render('Twój ruch', 1, 'gold')
                screen.blit(text, (275,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (155,530))
                text = font.render('Trafiony!', 1, 'white')
                screen.blit(text, (530,530))

                fun.rysuj_zaznaczenie(screen, 1*width/8, 530, 3*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 0
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 3:
            while True:
                if status_rozgrywki != 3:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10, 'black')

                font = pygame.font.Font(None, 75)
                text = font.render('Twój ruch', 1, 'gold')
                screen.blit(text, (275,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (155,530))
                text = font.render('Trafiony! Zatopiony!', 1, 'white')
                screen.blit(text, (437,530))

                fun.rysuj_zaznaczenie(screen, 1*width/8, 530, 3*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 0
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 4:
            while True:
                if status_rozgrywki != 4:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10, 'black')

                font = pygame.font.Font(None, 75)
                text = font.render('Twój ruch', 1, 'gold')
                screen.blit(text, (275,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (155,530))
                text = font.render('Zły wybór!', 1, 'white')
                screen.blit(text, (500,530))

                fun.rysuj_zaznaczenie(screen, 1*width/8, 530, 3*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 0
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 5:
            while True:
                if status_rozgrywki != 5:
                    break
                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                font = pygame.font.Font(None, 75)
                text = font.render('Ruch komputera', 1, 'gold')
                screen.blit(text, (195,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (558,530))
                text = font.render('Pudło!', 1, 'white')
                screen.blit(text, (155,530))

                fun.rysuj_zaznaczenie(screen, wyborXpoczatek + 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), wyborXpoczatek + przesuniecieX - 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + przesuniecieY - 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), 'black')
                fun.rysuj_zaznaczenie(screen, 5*width/8, 530, 7*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 0
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 6:
            while True:
                if status_rozgrywki != 6:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                font = pygame.font.Font(None, 75)
                text = font.render('Ruch komputera', 1, 'gold')
                screen.blit(text, (195,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (558,530))
                text = font.render('Trafiony!', 1, 'white')
                screen.blit(text, (155,530))

                fun.rysuj_zaznaczenie(screen, wyborXpoczatek + 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), wyborXpoczatek + przesuniecieX - 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + przesuniecieY - 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), 'black')
                fun.rysuj_zaznaczenie(screen, 5*width/8, 530, 7*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 8
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 7:
            while True:
                if status_rozgrywki != 7:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                font = pygame.font.Font(None, 75)
                text = font.render('Ruch komputera', 1, 'gold')
                screen.blit(text, (195,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Dalej', 1, 'white')
                screen.blit(text, (558,530))
                text = font.render('Trafiony! Zatopiony!', 1, 'white')
                screen.blit(text, (37,530))

                fun.rysuj_zaznaczenie(screen, wyborXpoczatek + 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), wyborXpoczatek + przesuniecieX - 10 - width/2 + przesuniecieX*(gra_gracz.ostatni_cel[0]-1), wyborYpoczatek + przesuniecieY - 10 + przesuniecieY*(gra_gracz.ostatni_cel[1]-1), 'black')
                fun.rysuj_zaznaczenie(screen, 5*width/8, 530, 7*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = 8
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == 8:
            while True:
                if status_rozgrywki != 8:
                    break

                status_rozgrywki = gra_gracz.ruch()

        else:
            spr = False

            while True:
                screen.fill('darkblue')

                font = pygame.font.Font(None, 75)
                if gra_komputer.liczba_niezniszczonych_statkow == 0:
                    text = font.render('Wygrałeś!', 1, 'gold')
                    screen.blit(text, (278, 25))



                    if spr == False and zpStat == 1:
                        try:
                            file = open('statGry.txt', 'r')
                            try:
                                statGry = int(file.readline().strip('\n'))
                                file.close()
                            except:
                                file = open('statGry.txt', 'w')
                                file.write('1')
                                file.close()
                                statGry = 1
                        except:
                            file = open('statGry.txt', 'w')
                            file.write('1')
                            file.close()
                            statGry = 1
                        
                        file = open('statGry.txt', 'w')
                        file.write(str(statGry + 1))
                        file.close()

                        try:
                            file = open('statWygrane.txt', 'r')
                            try:
                                statWygrane = int(file.readline().strip('\n'))
                                file.close()
                            except:
                                file = open('statWygrane.txt', 'w')
                                file.write('1')
                                file.close()
                                statWygrane = 1
                        except:
                            file = open('statWygrane.txt', 'w')
                            file.write('1')
                            file.close()
                            statWygrane = 1

                        file = open('statWygrane.txt', 'w')
                        file.write(str(statWygrane + 1))
                        file.close()

                else:
                    text = font.render('Przegrałeś...', 1, 'gold')
                    screen.blit(text, (250, 25))

                    if spr == False and zpStat == 1:
                        try:
                            file = open('statGry.txt', 'r')
                            try:
                                statGry = int(file.readline().strip('\n'))
                                file.close()
                            except:
                                file = open('statGry.txt', 'w')
                                file.write('1')
                                file.close()
                                statGry = 1
                        except:
                            file = open('statGry.txt', 'w')
                            file.write('1')
                            file.close()
                            statGry = 1
                        
                        file = open('statGry.txt', 'w')
                        file.write(str(statGry + 1))
                        file.close()

                font = pygame.font.Font(None, 35)
                text = font.render('Twoje statki', 1, 'steelblue')
                screen.blit(text, (125,115))
                text = font.render('Statki wroga', 1, 'steelblue')
                screen.blit(text, (525,115))
                text = font.render('Steruje komputer', 1, 'steelblue')
                screen.blit(text, (100,465))
                text = font.render('Sterujesz Ty', 1, 'steelblue')
                screen.blit(text, (525,465))
                
                gra_gracz.rysuj()
                gra_komputer.rysuj()

                font = pygame.font.Font(None, 50)
                text = font.render('Wróć', 1, 'white')
                screen.blit(text, (355,500))

                fun.rysuj_zaznaczenie(screen, 300, 500, 500, 500 + 35)

                spr = True
                        
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            return
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()