# -*- coding: utf-8 -*-

import pygame, sys, fun, gra, statki

def main(screen, width, height, pzTrud, zpStat):

    wybor = 200

    while True:
        screen.fill('darkblue')

        font = pygame.font.Font(None, 100)
        text = font.render('Graj', 1, 'gold')
        screen.blit(text, (330,50))
        font = pygame.font.Font(None, 45)
        text = font.render('Losuj ułożenie statków', 1, 'white')
        screen.blit(text, (233,205))
        font = pygame.font.Font(None, 45)
        text = font.render('Ustaw statki samodzielnie', 1, 'white')
        screen.blit(text, (205,305))
        font = pygame.font.Font(None, 50)
        text = font.render('Wróć', 1, 'white')
        screen.blit(text, (355,500))

        fun.rysuj_zaznaczenie(screen, 200, wybor, 600, wybor + 35)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if wybor > 200:
                        wybor -= 100
                    if wybor == 400:
                        wybor -= 100
                if event.key == pygame.K_DOWN:
                    if wybor < 500:
                        wybor += 100
                    if wybor == 400:
                        wybor += 100
                if event.key == pygame.K_RETURN:
                    if wybor == 200:
                        gra.main(screen, width, height, pzTrud, zpStat)
                        return
                    elif wybor == 300:
                        statki.main(screen, width, height, pzTrud, zpStat)
                        return
                    elif wybor == 500:
                        return
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()