# -*- coding: utf-8 -*-

import pygame, sys, fun

def main(screen, width, height):

    wybor = 500

    while True:
        screen.fill('darkblue')

        try:
            file = open('statGry.txt', 'r')
            try:
                statGry = int(file.readline().strip('\n'))
                file.close()
            except:
                file = open('statGry.txt', 'w')
                file.write('0')
                file.close()
                statGry = 0
        except:
            file = open('statGry.txt', 'w')
            file.write('0')
            file.close()
            statGry = 0

        try:
            file = open('statWygrane.txt', 'r')
            try:
                statWygrane = int(file.readline().strip('\n'))
                file.close()
            except:
                file = open('statWygrane.txt', 'w')
                file.write('0')
                file.close()
                statWygrane = 0
        except:
            file = open('statWygrane.txt', 'w')
            file.write('0')
            file.close()
            statWygrane = 0

        font = pygame.font.Font(None, 100)
        text = font.render('Statystyki', 1, 'gold')
        screen.blit(text, (225,50))
        font = pygame.font.Font(None, 50)
        text = font.render('Zakończone gry:           ' + str(statGry), 1, 'steelblue')
        screen.blit(text, (200,200))
        procent = 0
        if statGry != 0:
            procent = statWygrane*100/statGry
        text = font.render('Procent wygranych:    ' + str(int(procent)), 1, 'steelblue')
        screen.blit(text, (200,300))
        text = font.render('Wyzeruj', 1, 'white')
        screen.blit(text, (330,400))
        text = font.render('Wróć', 1, 'white')
        screen.blit(text, (355,500))

        fun.rysuj_zaznaczenie(screen, 300, wybor, 500, wybor + 35)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if wybor > 400:
                        wybor -= 100
                if event.key == pygame.K_DOWN:
                    if wybor < 500:
                        wybor += 100
                if event.key == pygame.K_RETURN:
                    if wybor == 400:
                        file = open('statGry.txt', 'w')
                        file.write('0')
                        file.close()
                        statGry = 0
                        file = open('statWygrane.txt', 'w')
                        file.write('0')
                        file.close()
                        statWygrane = 0
                    elif wybor == 500:
                        return
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()