# -*- coding: utf-8 -*-

import pygame, random, datetime

alfabet = ' ABCDEFGHIJ'
cyfry = ' 1234567890'

random.seed(datetime.datetime.now().timestamp())

def rysuj_zaznaczenie(screen, x0, y0, x1, y1, COLOR = 'white'):
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5
    pygame.draw.line(screen, COLOR, [x0, y0], [x1, y0], 1)
    pygame.draw.line(screen, COLOR, [x0, y0], [x0, y1], 1)
    pygame.draw.line(screen, COLOR, [x1, y0], [x1, y1], 1)
    pygame.draw.line(screen, COLOR, [x0, y1], [x1, y1], 1)

class Element:
    #status
    #  -1 - element pomocniczy (oznaczenie siatki)
    #   0 - jeszcze nie wybrano
    #   1 - już wybrano
    def __init__(self, x, y, sX, sY, i, j):
        self.i = i
        self.j = j
        self.sX = sX
        self.sY = sY
        self.x = x+self.i*self.sX
        self.y = y+self.j*self.sY
        self.status = 0
        self.text = ''
        self.przynaleznosc = None
    def zmien_opcje(self, x, y, sX, sY, i, j):
        self.i = i
        self.j = j
        self.sX = sX
        self.sY = sY
        self.x = x+self.i*self.sX
        self.y = y+self.j*self.sY
        if self.status == 1:
            self.status = 0
    def rysuj(self, screen):
        if self.status == -1:
            pygame.draw.rect(screen, 'midnightblue', [self.x, self.y, self.sX, self.sY])
            rysuj_zaznaczenie(screen, self.x+5, self.y+5, self.x + self.sX-5, self.y + self.sY-5)
            font = pygame.font.Font(None, 50)
            text = font.render(self.text, 1, 'white')
            screen.blit(text, (self.x+self.sX/4, self.y+self.sY/8))
        elif self.status == 0:
            COLOR = 'black'
            if self.przynaleznosc != None:
                if self.przynaleznosc.tryb == 0:
                    if self.przynaleznosc.status == 0:
                        COLOR = 'darkgreen'
                    elif self.przynaleznosc.status == 1:
                        COLOR = 'darkgreen'
                    elif self.przynaleznosc.status == 2:
                        COLOR = 'darkred'
            pygame.draw.rect(screen, COLOR, [self.x, self.y, self.sX, self.sY])
            rysuj_zaznaczenie(screen, self.x+5, self.y+5, self.x + self.sX-5, self.y + self.sY-5)
        else:
            COLOR = 'steelblue'
            if self.przynaleznosc != None:
                if self.przynaleznosc.status == 0:
                    COLOR = 'darkgreen'
                elif self.przynaleznosc.status == 1:
                    COLOR = 'goldenrod'
                elif self.przynaleznosc.status == 2:
                    COLOR = 'darkred'
            pygame.draw.rect(screen, COLOR, [self.x, self.y, self.sX, self.sY])
            rysuj_zaznaczenie(screen, self.x+5, self.y+5, self.x + self.sX-5, self.y + self.sY-5)

class Siatka:
    def __init__(self, screen, x, y, width, height, m, n):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.m = m + 1  # liczba rzędów (+1 rząd na oznaczenia)
        self.n = n + 1  # liczba kolumn (+1 kolumna na oznaczenia)
        self.sX = self.width / self.m
        self.sY = self.height / self.n
        self.screen = screen
        self.elementy = [[Element(x, y, self.sX, self.sY, i, j) for i in range(self.m)] for j in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                if i == 0:
                    self.elementy[i][j].status = -1
                    self.elementy[i][j].text = alfabet[j]
                if j == 0:
                    self.elementy[i][j].status = -1
                    self.elementy[i][j].text = cyfry[i]
    def zmien_opcje(self, screen, x, y, width, height, m, n):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.m = m + 1  # liczba rzędów (+1 rząd na oznaczenia)
        self.n = n + 1  # liczba kolumn (+1 kolumna na oznaczenia)
        self.sX = self.width / self.m
        self.sY = self.height / self.n
        self.screen = screen
        for i in range(self.m):
            for j in range(self.n):
                self.elementy[i][j].zmien_opcje(x, y, self.sX, self.sY, j, i)
    def rysuj(self):
        rysuj_zaznaczenie(self.screen, self.x + 4, self.y + 4, self.x + self.width - 5, self.y + self.height - 5)
        for i in range(self.m):
            for j in range(self.n):
                self.elementy[i][j].rysuj(self.screen)

class Statek:
    #status
    #   0 - nietrafiony
    #   1 - trafiony
    #   2 - zatopiony
    def __init__(self, tryb, i, elementy):
        self.tryb = tryb
        self.pozostala_dlugosc = i
        self.status = 0
        self.elementy = elementy
        for element in self.elementy:
            element.przynaleznosc = self

class Gra:
    def __init__(self, screen, x, y, width, height, tryb, L, trudnosc, ust = False):
        self.tryb = tryb    # 0 - gracz, 1 - komputer
        self.siatka = Siatka(screen, x, y, width, height, L, L)
        self.statki = []
        self.trudnosc = trudnosc
        if ust == True:
            pass
        else:
            self.losuj_statki()
            self.liczba_niezniszczonych_statkow = len(self.statki)
            if self.tryb == 0:
                self.kolejka = []
                self.ostatni_udany_cel = None
                self.ostatni_cel = None
    def zmien_opcje(self, screen, x, y, width, height, tryb, L, pzTrud, ust):
        self.tryb = tryb    # 0 - gracz, 1 - komputer
        self.siatka.zmien_opcje(screen, x, y, width, height, L, L)
        self.liczba_niezniszczonych_statkow = len(self.statki)
        if self.tryb == 0:
            self.kolejka = []
            self.ostatni_udany_cel = None
            self.ostatni_cel = None
        for stat in self.statki:
            stat.tryb = self.tryb
        return self
    def rysuj(self):
        self.siatka.rysuj()
    def sprawdzenie_okolicy(self, i, j):
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                if a == i and b == j:
                    continue
                if (a > self.siatka.m - 1) or (b > self.siatka.n - 1):
                    continue
                if self.siatka.elementy[a][b].status == 1:
                    if self.siatka.elementy[a][b].przynaleznosc != None:
                        #print(a, b)
                        if self.siatka.elementy[a][b].przynaleznosc.status == 2:
                            #print('t2')
                            return True
        return False
    def ruch(self, i = 0, j = 0):
        if self.tryb == 0:
            while True:
                if self.trudnosc == 0:
                    break
                else:
                    if len(self.kolejka) == 0:
                        break
                    element = self.kolejka.pop(random.randint(0, len(self.kolejka) - 1))
                    i = element[0]
                    j = element[1]
                    if self.siatka.elementy[i][j].status != 0:
                        continue
                    if self.sprawdzenie_okolicy(i, j) == True and self.trudnosc == 2:
                        continue
                    self.siatka.elementy[i][j].status = 1
                    self.ostatni_cel = [j, i]
                    if self.siatka.elementy[i][j].przynaleznosc != None:
                        self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc -= 1
                        if self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc == 0:
                            self.siatka.elementy[i][j].przynaleznosc.status = 2
                            self.liczba_niezniszczonych_statkow -= 1
                            self.kolejka.clear()
                            self.ostatni_udany_cel = None
                            return 7
                        else:
                            self.siatka.elementy[i][j].przynaleznosc.status = 1
                            if self.ostatni_udany_cel == None:
                                print('test')
                                if (0 <= (i - 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                                    self.kolejka.append([i - 1, j])
                                if (0 <= (i) < self.siatka.m) & (0 <= (j - 1) < self.siatka.n):
                                    self.kolejka.append([i, j - 1])
                                if (0 <= (i + 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                                    self.kolejka.append([i + 1, j])
                                if (0 <= (i) < self.siatka.m) & (0 <= (j + 1) < self.siatka.n):
                                    self.kolejka.append([i, j + 1])
                                self.ostatni_udany_cel = [i, j]
                            else:
                                if self.ostatni_udany_cel[0] == i:
                                    while True:
                                        for a in range(len(self.kolejka)):
                                            if self.kolejka[a][0] != i:
                                                self.kolejka.pop(a)
                                                break
                                        break
                                    if (0 <= (i) < self.siatka.m) & (0 <= (j - 1) < self.siatka.n):
                                        self.kolejka.append([i, j - 1])
                                    if (0 <= (i) < self.siatka.m) & (0 <= (j + 1) < self.siatka.n):
                                        self.kolejka.append([i, j + 1])
                                    self.ostatni_udany_cel = [i, j]
                                elif self.ostatni_udany_cel[1] == j:
                                    while True:
                                        for a in range(len(self.kolejka)):
                                            if self.kolejka[a][1] != j:
                                                self.kolejka.pop(a)
                                                break
                                        break
                                    if (0 <= (i - 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                                        self.kolejka.append([i - 1, j])
                                    if (0 <= (i + 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                                        self.kolejka.append([i + 1, j])
                                    self.ostatni_udany_cel = [i, j]
                            return 6
                    return 5
            while True:
                i = random.randint(1, self.siatka.m - 1)
                j = random.randint(1, self.siatka.n - 1)
                if self.siatka.elementy[i][j].status == 0:
                    if self.trudnosc < 2:
                        break
                    elif self.sprawdzenie_okolicy(i, j) == False:
                        break
            self.siatka.elementy[i][j].status = 1
            self.ostatni_cel = [j, i]
            if self.siatka.elementy[i][j].przynaleznosc != None:
                self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc -= 1
                if self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc == 0:
                    self.siatka.elementy[i][j].przynaleznosc.status = 2
                    self.liczba_niezniszczonych_statkow -= 1
                    self.kolejka.clear()
                    self.ostatni_udany_cel = None
                    return 7
                else:
                    self.siatka.elementy[i][j].przynaleznosc.status = 1
                    if (0 <= (i - 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                        self.kolejka.append([i - 1, j])
                    if (0 <= (i) < self.siatka.m) & (0 <= (j - 1) < self.siatka.n):
                        self.kolejka.append([i, j - 1])
                    if (0 <= (i + 1) < self.siatka.m) & (0 <= (j) < self.siatka.n):
                        self.kolejka.append([i + 1, j])
                    if (0 <= (i) < self.siatka.m) & (0 <= (j + 1) < self.siatka.n):
                        self.kolejka.append([i, j + 1])
                    self.ostatni_udany_cel = [i, j]
                    return 6
            return 5
        else:
            if self.siatka.elementy[i][j].status == 0:
                self.siatka.elementy[i][j].status = 1
                self.ostatni_cel = [j, i]
                if self.siatka.elementy[i][j].przynaleznosc != None:
                    self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc -= 1
                    if self.siatka.elementy[i][j].przynaleznosc.pozostala_dlugosc == 0:
                        self.siatka.elementy[i][j].przynaleznosc.status = 2
                        self.liczba_niezniszczonych_statkow -= 1
                        return 3
                    else:
                        self.siatka.elementy[i][j].przynaleznosc.status = 1
                        return 2
                return 1
            else:
                return 4
    
    def losuj_statki(self):
        liczba_statkow = 4

        while liczba_statkow > 0:
            spr = False

            orient = random.randint(1, 2)   # 1 - pozioma, 2 - pionowa
            if orient == 1:
                pierw_elX = random.randint(1, self.siatka.m - 1)
                pierw_elY = random.randint(1, self.siatka.n - 1)
                for i in range(pierw_elY, pierw_elY + liczba_statkow):
                    if i >= self.siatka.n:
                        spr = True
                        break
                    if self.siatka.elementy[pierw_elX][i].przynaleznosc != None:
                        spr = True
                        break
                    for a in range(pierw_elX - 1, pierw_elX + 2):
                        for b in range(i - 1, i + 2):
                            if 0 <= a < self.siatka.m:
                                if 0 <= b < self.siatka.n:
                                    if self.siatka.elementy[a][b].przynaleznosc != None:
                                        spr = True
                                        break
                if spr == False:
                    statki = []
                    for i in range(pierw_elY, pierw_elY + liczba_statkow):
                        statki.append(self.siatka.elementy[pierw_elX][i])
                    self.statki.append(Statek(self.tryb, liczba_statkow, statki))
                    liczba_statkow -= 1
            else:
                pierw_elX = random.randint(1, self.siatka.m - 1)
                pierw_elY = random.randint(1, self.siatka.n - 1)
                for i in range(pierw_elX, pierw_elX + liczba_statkow):
                    if i >= self.siatka.m:
                        spr = True
                        break
                    if self.siatka.elementy[i][pierw_elY].przynaleznosc != None:
                        spr = True
                        break
                    for a in range(i - 1, i + 2):
                        for b in range(pierw_elY - 1, pierw_elY + 2):
                            if 0 <= a < self.siatka.m:
                                if 0 <= b < self.siatka.n:
                                    if self.siatka.elementy[a][b].przynaleznosc != None:
                                        spr = True
                                        break
                if spr == False:
                    statki = []
                    for i in range(pierw_elX, pierw_elX + liczba_statkow):
                        statki.append(self.siatka.elementy[i][pierw_elY])
                    self.statki.append(Statek(self.tryb, liczba_statkow, statki))
                    liczba_statkow -= 1