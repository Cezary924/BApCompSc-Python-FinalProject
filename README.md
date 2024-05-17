# Projekt zaliczeniowy - Python

Tytul: _Program - gra Statki_

Autor: _Cezary924_

Jezyk: _Python_

Rok: _2022/2023_


## Wprowadzenie 
Gra „Statki” napisana została w języku Python z użyciem biblioteki PyGame jako 
projekt końcowy w ramach przedmiotu Język Python. Wybrany temat projektu pokrywa 
się z jednym z tematów zaproponowanych na stronie wykładowej. 


## Uruchomienie 
Uruchomić grę można z poziomu wiersza poleceń. Należy otworzyć wiersz poleceń 
w folderze z plikami gry i następnie wprowadzić komendę: _python main.py_. 


## Sterowanie 
Zarówno po opcjach w menu jak i planszach poruszać się można przy pomocy klawiszy 
strzałek. Wybór zaznaczonej opcji, dokonanie strzału lub zatwierdzenie lokalizacji statku 
odbywa się przy pomocy klawisza _ENTER_. Natomiast w trybie rozmieszczania statków na 
planszy oznaczanie pól odbywa się poprzez wciśnięcie klawisza _SPACE_. Dodatkowo na 
każdym ekranie wcisnąć można klawisz _ESCAPE_, który skutkuje powrotem do poprzedniego 
ekranu/menu. Krótkie przypomnienie zasad sterowania dostępne jest również w samej grze – opcja Sterowanie w Menu głównym. 


## Zasady gry 
Zasady zostały „żywcem wzięte” z niekomputerowego pierwowzoru. Plansze 
odpowiadające więc fragmentom morza podzielone zostały na 36 pól (6x6). Każdy z graczy 
posiada po jednym statku każdego typu (4–, 3–, 2–, 1–częściowy). Gra przebiega 
naprzemiennie pomiędzy graczami (graczem–użytkownikiem i graczem–komputerem). Każdy 
z graczy oddaje strzały, dopóki nie chybi – wtedy kontrola i możliwość strzałów przekazana 
zostaje drugiemu. Gra kończy się w momencie, gdy jeden z graczy zatopi wszystkie statki 
przeciwnika. 


## Opisy poszczególnych funkcjonalności menu
- Menu → Graj: wybranie go przez użytkownika powoduje wyświetlenie specjalnego ekranu 
z możliwością wyboru czy statki użytkownika mają zostać wylosowane czy 
użytkownik chce rozmieścić je samodzielnie. Wybranie opcji z losowaniem 
powoduje natychmiastowe przejście do gry. Natomiast opcja 
z rozmieszczeniem powoduje najpierw wyświetlenie ekranu, na którym krok 
po kroku umieszcza się statki zgodnie z wyświetlanymi informacjami i dopiero 
później przejście do samej gry. 
- Menu → Statystyki: wybranie go przez użytkownika powoduje wyświetlenie specjalnego 
ekranu z informacją o zgromadzonych statystykach. Wyświetlana jest 
ogólna liczba zakończonych rozgrywek oraz procentowa wartość 
wygranych rozgrywek względem wszystkich zakończonych. 
- Menu → Sterowanie: wybranie go przez użytkownika powoduje wyświetlenie specjalnego 
ekranu z informacją o używanych do sterowania klawiszach. 
- Menu → Ustawienia: wybranie go przez użytkownika powoduje wyświetlenie specjalnego 
ekranu z możliwością wyboru trybu trudności gry oraz wyboru czy gra 
ma gromadzić statystyki czy nie. 
- Menu → Informacje: wybranie go przez użytkownika powoduje wyświetlenie specjalnego 
ekranu ze zbiorem informacji o grze i jej autorze. 
- Menu → Wyjście: wybranie go przez użytkownika powoduje zakończenie działania gry. 