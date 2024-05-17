# -*- coding: utf-8 -*-

import pygame, sys, fun, gra, random

def zwroc_minimum(elementy, i):
    min = elementy[0][i]
    for el in elementy:
        if el[i] < min:
            min = el[i]
    return min

def sprawdzenie_poprawnosci(elementy, siatka, liczba_statkow):
    spr = False

    orient = 0 # 1 - pozioma, 2 - pionowa
    if len(elementy) == 1:
        orient = 1
    elif elementy[0][0] == elementy[1][0]:
        orient = 1
    else:
        orient = 2
    if orient == 1:
        pierw_elX = zwroc_minimum(elementy, 0)
        pierw_elY = zwroc_minimum(elementy, 1)
        for i in range(pierw_elY, pierw_elY + liczba_statkow):
            if i >= siatka.n:
                spr = True
                break
            if siatka.elementy[pierw_elX][i].przynaleznosc != None:
                spr = True
                break
            for a in range(pierw_elX - 1, pierw_elX + 2):
                for b in range(i - 1, i + 2):
                    if 0 <= a < siatka.m:
                        if 0 <= b < siatka.n:
                            if siatka.elementy[a][b].przynaleznosc != None:
                                spr = True
                                break

    else:
        pierw_elX = zwroc_minimum(elementy, 0)
        pierw_elY = zwroc_minimum(elementy, 1)
        for i in range(pierw_elX, pierw_elX + liczba_statkow):
            if i >= siatka.m:
                spr = True
                break
            if siatka.elementy[i][pierw_elY].przynaleznosc != None:
                spr = True
                break
            for a in range(i - 1, i + 2):
                for b in range(pierw_elY - 1, pierw_elY + 2):
                    if 0 <= a < siatka.m:
                        if 0 <= b < siatka.n:
                            if siatka.elementy[a][b].przynaleznosc != None:
                                spr = True
                                break
        
    if spr == False:
        return True
    else:
        return False

def main(screen, width, height, pzTrud, zpStat):

    liczba_rzedow_i_kolumn = 6
    gra_komputer = fun.Gra(screen, 450, 150, 301, 301, 1, liczba_rzedow_i_kolumn, pzTrud, True)

    przesuniecieX = gra_komputer.siatka.sX
    przesuniecieY = gra_komputer.siatka.sY
    wyborX = gra_komputer.siatka.x + przesuniecieX
    wyborY = gra_komputer.siatka.y + przesuniecieY
    wyborXpoczatek = wyborX
    wyborYpoczatek = wyborY
    X = 1
    Y = 1

    # 0 - 4czesciowy
    # 1 - 3czesciowy
    # 2 - 2czesciowy
    # 3 - 1czesciowy
    # -1 - źle
    status_rozgrywki = 0
    poprzedni_status_rozgrywki = 0

    statki = []

    while True:
        if status_rozgrywki == 0:
            while True:
                if status_rozgrywki != 0:
                    break

                screen.fill('darkblue')
                
                font = pygame.font.Font(None, 35)
                text = font.render('Wyznacz na siatce', 1, 'steelblue')
                screen.blit(text, (75,170))
                text = font.render('lokalizację statków.', 1, 'steelblue')
                screen.blit(text, (75,200))
                text = font.render('Musisz stworzyć po', 1, 'steelblue')
                screen.blit(text, (75,230))
                text = font.render('jednym statku każdego', 1, 'steelblue')
                screen.blit(text, (75,260))
                text = font.render('rozmiaru (1-4 kafelków).', 1, 'steelblue')
                screen.blit(text, (75,290))
                text = font.render('Statki nie mogą się dotykać.', 1, 'steelblue')
                screen.blit(text, (75,320))
                text = font.render('Wyznacz 4-częściowy statek.', 1, 'steelblue')
                screen.blit(text, (75,380))
                text = font.render('Następnie zatwierdź go.', 1, 'steelblue')
                screen.blit(text, (75,410))
                
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10)

                font = pygame.font.Font(None, 75)
                text = font.render('Ustaw statki', 1, 'gold')
                screen.blit(text, (247,25))

                poprzedni_status_rozgrywki = status_rozgrywki

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            elementy = []
                            for i in range(gra_komputer.siatka.m):
                                for j in range(gra_komputer.siatka.n):
                                    if i == 0:
                                        continue
                                    if j == 0:
                                        continue
                                    if gra_komputer.siatka.elementy[i][j].status == 1:
                                        if gra_komputer.siatka.elementy[i][j].przynaleznosc == None:
                                            elementy.append([i, j])
                            if len(elementy) != 4:
                                status_rozgrywki = -1
                                break
                            else:
                                if elementy[0][0] != elementy[1][0]:
                                    if elementy[0][1] != elementy[1][1]:
                                        status_rozgrywki = -1
                                        break   
                                    elif elementy[0][1] != elementy[2][1]:
                                        status_rozgrywki = -1
                                        break
                                    elif elementy[0][1] != elementy[3][1]:
                                        status_rozgrywki = -1
                                        break 
                                elif elementy[0][0] != elementy[2][0]:
                                    status_rozgrywki = -1
                                    break
                                elif elementy[0][0] != elementy[3][0]:
                                    status_rozgrywki = -1
                                    break
                                if sprawdzenie_poprawnosci(elementy, gra_komputer.siatka, 4) == False:
                                    status_rozgrywki = -1
                                    break
                                statki.append(elementy)
                                elementy_siatki = []
                                for el in elementy:
                                    elementy_siatki.append(gra_komputer.siatka.elementy[el[0]][el[1]])
                                gra_komputer.statki.append(fun.Statek(gra_komputer.tryb, len(elementy_siatki), elementy_siatki))
                                elementy.clear()
                                status_rozgrywki = 1
                                break
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
                        if event.key == pygame.K_SPACE:
                            if gra_komputer.siatka.elementy[Y][X].status == 0:
                                gra_komputer.siatka.elementy[Y][X].status = 1
                            elif gra_komputer.siatka.elementy[Y][X].status == 1 and gra_komputer.siatka.elementy[Y][X].przynaleznosc != None:
                                pass
                            else:
                                gra_komputer.siatka.elementy[Y][X].status = 0
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        if status_rozgrywki == 1:
            while True:
                if status_rozgrywki != 1:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Wyznacz na siatce', 1, 'steelblue')
                screen.blit(text, (75,170))
                text = font.render('lokalizację statków.', 1, 'steelblue')
                screen.blit(text, (75,200))
                text = font.render('Musisz stworzyć po', 1, 'steelblue')
                screen.blit(text, (75,230))
                text = font.render('jednym statku każdego', 1, 'steelblue')
                screen.blit(text, (75,260))
                text = font.render('rozmiaru (1-4 kafelków).', 1, 'steelblue')
                screen.blit(text, (75,290))
                text = font.render('Statki nie mogą się dotykać.', 1, 'steelblue')
                screen.blit(text, (75,320))
                text = font.render('Wyznacz 3-częściowy statek.', 1, 'steelblue')
                screen.blit(text, (75,380))
                text = font.render('Następnie zatwierdź go.', 1, 'steelblue')
                screen.blit(text, (75,410))
                
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10)

                font = pygame.font.Font(None, 75)
                text = font.render('Ustaw statki', 1, 'gold')
                screen.blit(text, (247,25))

                poprzedni_status_rozgrywki = status_rozgrywki

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            elementy = []
                            for i in range(gra_komputer.siatka.m):
                                for j in range(gra_komputer.siatka.n):
                                    if i == 0:
                                        continue
                                    if j == 0:
                                        continue
                                    if gra_komputer.siatka.elementy[i][j].status == 1:
                                        if gra_komputer.siatka.elementy[i][j].przynaleznosc == None:
                                            elementy.append([i, j])
                            if len(elementy) != 3:
                                status_rozgrywki = -1
                                break
                            else:
                                if elementy[0][0] != elementy[1][0]:
                                    if elementy[0][1] != elementy[1][1]:
                                        status_rozgrywki = -1
                                        break   
                                    elif elementy[0][1] != elementy[2][1]:
                                        status_rozgrywki = -1
                                        break
                                elif elementy[0][0] != elementy[2][0]:
                                    status_rozgrywki = -1
                                    break
                                if sprawdzenie_poprawnosci(elementy, gra_komputer.siatka, 3) == False:
                                    status_rozgrywki = -1
                                    break
                                statki.append(elementy)
                                elementy_siatki = []
                                for el in elementy:
                                    elementy_siatki.append(gra_komputer.siatka.elementy[el[0]][el[1]])
                                gra_komputer.statki.append(fun.Statek(gra_komputer.tryb, len(elementy_siatki), elementy_siatki))
                                elementy.clear()
                                status_rozgrywki = 2
                                break
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
                        if event.key == pygame.K_SPACE:
                            if gra_komputer.siatka.elementy[Y][X].status == 0:
                                gra_komputer.siatka.elementy[Y][X].status = 1
                            elif gra_komputer.siatka.elementy[Y][X].status == 1 and gra_komputer.siatka.elementy[Y][X].przynaleznosc != None:
                                pass
                            else:
                                gra_komputer.siatka.elementy[Y][X].status = 0
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()


        if status_rozgrywki == 2:
            while True:
                if status_rozgrywki != 2:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Wyznacz na siatce', 1, 'steelblue')
                screen.blit(text, (75,170))
                text = font.render('lokalizację statków.', 1, 'steelblue')
                screen.blit(text, (75,200))
                text = font.render('Musisz stworzyć po', 1, 'steelblue')
                screen.blit(text, (75,230))
                text = font.render('jednym statku każdego', 1, 'steelblue')
                screen.blit(text, (75,260))
                text = font.render('rozmiaru (1-4 kafelków).', 1, 'steelblue')
                screen.blit(text, (75,290))
                text = font.render('Statki nie mogą się dotykać.', 1, 'steelblue')
                screen.blit(text, (75,320))
                text = font.render('Wyznacz 2-częściowy statek.', 1, 'steelblue')
                screen.blit(text, (75,380))
                text = font.render('Następnie zatwierdź go.', 1, 'steelblue')
                screen.blit(text, (75,410))
                
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10)

                font = pygame.font.Font(None, 75)
                text = font.render('Ustaw statki', 1, 'gold')
                screen.blit(text, (247,25))

                poprzedni_status_rozgrywki = status_rozgrywki

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            elementy = []
                            for i in range(gra_komputer.siatka.m):
                                for j in range(gra_komputer.siatka.n):
                                    if i == 0:
                                        continue
                                    if j == 0:
                                        continue
                                    if gra_komputer.siatka.elementy[i][j].status == 1:
                                        if gra_komputer.siatka.elementy[i][j].przynaleznosc == None:
                                            elementy.append([i, j])
                            if len(elementy) != 2:
                                status_rozgrywki = -1
                                break
                            else:
                                if elementy[0][0] != elementy[1][0]:
                                    if elementy[0][1] != elementy[1][1]:
                                        status_rozgrywki = -1
                                        break
                                if sprawdzenie_poprawnosci(elementy, gra_komputer.siatka, 2) == False:
                                    status_rozgrywki = -1
                                    break
                                statki.append(elementy)
                                elementy_siatki = []
                                for el in elementy:
                                    elementy_siatki.append(gra_komputer.siatka.elementy[el[0]][el[1]])
                                gra_komputer.statki.append(fun.Statek(gra_komputer.tryb, len(elementy_siatki), elementy_siatki))
                                elementy.clear()
                                status_rozgrywki = 3
                                break
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
                        if event.key == pygame.K_SPACE:
                            if gra_komputer.siatka.elementy[Y][X].status == 0:
                                gra_komputer.siatka.elementy[Y][X].status = 1
                            elif gra_komputer.siatka.elementy[Y][X].status == 1 and gra_komputer.siatka.elementy[Y][X].przynaleznosc != None:
                                pass
                            else:
                                gra_komputer.siatka.elementy[Y][X].status = 0
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()


        if status_rozgrywki == 3:
            while True:
                if status_rozgrywki != 3:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Wyznacz na siatce', 1, 'steelblue')
                screen.blit(text, (75,170))
                text = font.render('lokalizację statków.', 1, 'steelblue')
                screen.blit(text, (75,200))
                text = font.render('Musisz stworzyć po', 1, 'steelblue')
                screen.blit(text, (75,230))
                text = font.render('jednym statku każdego', 1, 'steelblue')
                screen.blit(text, (75,260))
                text = font.render('rozmiaru (1-4 kafelków).', 1, 'steelblue')
                screen.blit(text, (75,290))
                text = font.render('Statki nie mogą się dotykać.', 1, 'steelblue')
                screen.blit(text, (75,320))
                text = font.render('Wyznacz 1-częściowy statek.', 1, 'steelblue')
                screen.blit(text, (75,380))
                text = font.render('Następnie zatwierdź go.', 1, 'steelblue')
                screen.blit(text, (75,410))
                
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10)

                font = pygame.font.Font(None, 75)
                text = font.render('Ustaw statki', 1, 'gold')
                screen.blit(text, (247,25))

                poprzedni_status_rozgrywki = status_rozgrywki

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            elementy = []
                            for i in range(gra_komputer.siatka.m):
                                for j in range(gra_komputer.siatka.n):
                                    if i == 0:
                                        continue
                                    if j == 0:
                                        continue
                                    if gra_komputer.siatka.elementy[i][j].status == 1:
                                        if gra_komputer.siatka.elementy[i][j].przynaleznosc == None:
                                            elementy.append([i, j])
                            if len(elementy) != 1:
                                status_rozgrywki = -1
                                break
                            else:
                                if sprawdzenie_poprawnosci(elementy, gra_komputer.siatka, 1) == False:
                                    status_rozgrywki = -1
                                    break
                                statki.append(elementy)
                                elementy_siatki = []
                                for el in elementy:
                                    elementy_siatki.append(gra_komputer.siatka.elementy[el[0]][el[1]])
                                gra_komputer.statki.append(fun.Statek(gra_komputer.tryb, len(elementy_siatki), elementy_siatki))
                                elementy.clear()
                                gra.main(screen, width, height, pzTrud, zpStat, True, gra_komputer)
                                return
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
                        if event.key == pygame.K_SPACE:
                            if gra_komputer.siatka.elementy[Y][X].status == 0:
                                gra_komputer.siatka.elementy[Y][X].status = 1
                            elif gra_komputer.siatka.elementy[Y][X].status == 1 and gra_komputer.siatka.elementy[Y][X].przynaleznosc != None:
                                pass
                            else:
                                gra_komputer.siatka.elementy[Y][X].status = 0
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()

        elif status_rozgrywki == -1:
            while True:
                if status_rozgrywki != -1:
                    break

                screen.fill('darkblue')

                font = pygame.font.Font(None, 35)
                text = font.render('Wyznacz na siatce', 1, 'steelblue')
                screen.blit(text, (75,170))
                text = font.render('lokalizację statków.', 1, 'steelblue')
                screen.blit(text, (75,200))
                text = font.render('Musisz stworzyć po', 1, 'steelblue')
                screen.blit(text, (75,230))
                text = font.render('jednym statku każdego', 1, 'steelblue')
                screen.blit(text, (75,260))
                text = font.render('rozmiaru (1-4 kafelków).', 1, 'steelblue')
                screen.blit(text, (75,290))
                text = font.render('Statki nie mogą się dotykać.', 1, 'steelblue')
                screen.blit(text, (75,320))
                
                gra_komputer.rysuj()

                fun.rysuj_zaznaczenie(screen, wyborX + 10, wyborY + 10, wyborX + przesuniecieX - 10, wyborY + przesuniecieY - 10, 'black')

                font = pygame.font.Font(None, 75)
                text = font.render('Ustaw statki', 1, 'gold')
                screen.blit(text, (247,25))

                font = pygame.font.Font(None, 50)
                text = font.render('Wróć', 1, 'white')
                screen.blit(text, (155,530))
                text = font.render('Źle!', 1, 'white')
                screen.blit(text, (565,530))

                fun.rysuj_zaznaczenie(screen, 1*width/8, 530, 3*width/8, 565)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            status_rozgrywki = poprzedni_status_rozgrywki
                            break
                        if event.key == pygame.K_ESCAPE:
                            return
                    if event.type == pygame.QUIT:
                        sys.exit()

                pygame.display.flip()