# -*- coding: utf-8 -*-

import pygame, sys, fun, gra, statystyki, informacje, menu_gra, sterowanie, ustawienia
pygame.init()

def main():
    
    pygame.display.set_caption('Gra Statki')

    img = pygame.image.load('boat.png')
    pygame.display.set_icon(img)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    wybor = 200

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

        font = pygame.font.Font(None, 100)
        text = font.render('Menu główne', 1, 'gold')
        screen.blit(text, (175,50))
        font = pygame.font.Font(None, 50)
        text = font.render('Graj', 1, 'white')
        screen.blit(text, (365,200))
        if zpStat == 1:
            text = font.render('Statystyki', 1, 'white')
            screen.blit(text, (315,260))
        text = font.render('Sterowanie', 1, 'white')
        screen.blit(text, (308,320))
        text = font.render('Ustawienia', 1, 'white')
        screen.blit(text, (308,380))
        text = font.render('Informacje', 1, 'white')
        screen.blit(text, (315,440))
        text = font.render('Wyjście', 1, 'white')
        screen.blit(text, (335,500))

        fun.rysuj_zaznaczenie(screen, 300, wybor, 500, wybor + 35)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if wybor > 200:
                        wybor -= 60
                    if zpStat == 0 and wybor == 260:
                        wybor -= 60
                if event.key == pygame.K_DOWN:
                    if wybor < 500:
                        wybor += 60
                    if zpStat == 0 and wybor == 260:
                        wybor += 60
                if event.key == pygame.K_RETURN:
                    if wybor == 200:
                        menu_gra.main(screen, width, height, pzTrud, zpStat)
                    elif wybor == 260:
                        statystyki.main(screen, width, height)
                    elif wybor == 320:
                        sterowanie.main(screen, width, height)
                    elif wybor == 380:
                        ustawienia.main(screen, width, height)
                    elif wybor == 440:
                        informacje.main(screen, width, height)
                    elif wybor == 500:
                        sys.exit()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()