# -*- coding: utf-8 -*-

import pygame, sys, fun

def main(screen, width, height):

    wybor = 500

    while True:
        screen.fill('darkblue')

        try:
            file = open('pzTrud.txt', 'r')
            try:
                pzTrud = int(file.readline().strip('\n'))
                file.close()
            except:
                file = open('pzTrud.txt', 'w')
                file.write('1')
                file.close()
                pzTrud = 1
        except:
            file = open('pzTrud.txt', 'w')
            file.write('1')
            file.close()
            pzTrud = 1

        try:
            file = open('zpStat.txt', 'r')
            try:
                zpStat = int(file.readline().strip('\n'))
                file.close()
            except:
                file = open('zpStat.txt', 'w')
                file.write('1')
                file.close()
                zpStat = 1
        except:
            file = open('zpStat.txt', 'w')
            file.write('1')
            file.close()
            zpStat = 1

        # pzTrud: 2 - trudny
        #         1 - średni
        #         0 - łatwy
        # zpStat: 1 - zapisywanie statystyk włączone
        #         0 - zapisywanie statystyk wyłączone

        font = pygame.font.Font(None, 100)
        text = font.render('Ustawienia', 1, 'gold')
        screen.blit(text, (215,50))
        font = pygame.font.Font(None, 50)
        if pzTrud == 0:
            pzTrudStr = "  Łatwy"
        elif pzTrud == 1:
            pzTrudStr = " Średni"
        else:
            pzTrudStr = "Trudny"
        text = font.render('Poziom trudności: ' + pzTrudStr, 1, 'white')
        screen.blit(text, (190,200))
        if zpStat == 0:
            zpStatStr = "Wył."
        else:
            zpStatStr = "  Wł."
        text = font.render('Gromadzenie statystyk: ' + zpStatStr, 1, 'white')
        screen.blit(text, (160,300))
        text = font.render('Ustawienia domyślne', 1, 'white')
        screen.blit(text, (220,400))
        text = font.render('Wróć', 1, 'white')
        screen.blit(text, (355,500))

        fun.rysuj_zaznaczenie(screen, 150, wybor, 650, wybor + 35)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if wybor > 200:
                        wybor -= 100
                if event.key == pygame.K_DOWN:
                    if wybor < 500:
                        wybor += 100
                if event.key == pygame.K_RETURN:
                    if wybor == 200:
                        if pzTrud == 0:
                            file = open('pzTrud.txt', 'w')
                            file.write('1')
                            file.close()
                            pzTrud = 1
                        elif pzTrud == 1:
                            file = open('pzTrud.txt', 'w')
                            file.write('2')
                            file.close()
                            pzTrud = 2
                        else:
                            file = open('pzTrud.txt', 'w')
                            file.write('0')
                            file.close()
                            pzTrud = 0
                    if wybor == 300:
                        if zpStat == 0:
                            file = open('zpStat.txt', 'w')
                            file.write('1')
                            file.close()
                            zpStat = 1
                        else:
                            file = open('zpStat.txt', 'w')
                            file.write('0')
                            file.close()
                            zpStat = 0
                    if wybor == 400:
                        file = open('pzTrud.txt', 'w')
                        file.write('1')
                        file.close()
                        pzTrud = 1
                        file = open('zpStat.txt', 'w')
                        file.write('1')
                        file.close()
                        zpStat = 1
                    elif wybor == 500:
                        return
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()