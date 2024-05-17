# -*- coding: utf-8 -*-

import pygame, sys, fun

def main(screen, width, height):

    wybor = 500

    while True:
        screen.fill('darkblue')

        font = pygame.font.Font(None, 50)
        text = font.render('Gra Statki', 1, 'steelblue')
        screen.blit(text, (320,180))
        text = font.render('Projekt końcowy', 1, 'steelblue')
        screen.blit(text, (270,230))
        text = font.render('Język Python', 1, 'steelblue')
        screen.blit(text, (300,280))
        text = font.render('Cezary924', 1, 'steelblue')
        screen.blit(text, (250,330))
        text = font.render('2022/2023', 1, 'steelblue')
        screen.blit(text, (320,380))

        font = pygame.font.Font(None, 100)
        text = font.render('Informacje', 1, 'gold')
        screen.blit(text, (225,50))
        font = pygame.font.Font(None, 50)
        text = font.render('Wróć', 1, 'white')
        screen.blit(text, (355,500))

        fun.rysuj_zaznaczenie(screen, 300, wybor, 500, wybor + 35)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if wybor == 500:
                        return
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()