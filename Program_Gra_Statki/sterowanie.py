import pygame, sys, fun

def main(screen, width, height):

    wybor = 500

    while True:
        screen.fill('darkblue')

        font = pygame.font.Font(None, 30)
        text = font.render('STRZAŁKI:     zmiana lokalizacji wskaźnika', 1, 'steelblue')
        screen.blit(text, (196,180))
        text = font.render('SPACJA:                    wyznaczanie statków', 1, 'steelblue')
        screen.blit(text, (196,255))
        text = font.render('ENTER:               zatwierdzanie akcji/strzał', 1, 'steelblue')
        screen.blit(text, (196,330))
        text = font.render('ESCAPE:   powrót do poprzedniego ekranu', 1, 'steelblue')
        screen.blit(text, (196,405))

        font = pygame.font.Font(None, 100)
        text = font.render('Sterowanie', 1, 'gold')
        screen.blit(text, (210,50))
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