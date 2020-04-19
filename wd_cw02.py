# ZADANIE 1
import sys

def zadanie_1():
    print("Podaj zdanie: ")
    napis =  sys.stdin.readline()
    print('w podanym napisie spacja pojawia się:', napis.count(' '))

# ZADANIE 2
def zadanie_2():
    print('Podaj liczbe:')
    liczba_1 = sys.stdin.readline()
    print('Podaj drugą liczbe:')
    liczba_2 = sys.stdin.readline()
    sys.stdout.write('wynik: '+str(float(liczba_1)*float(liczba_2)))

# ZADANIE 3
def zadanie_3():
    print('Lista operatorów w instrukcjach warunkowych')
    print('Równe: a == b')
    print('Różne: a != b')
    print('Mniejsze: a < b')
    print('Mniejsze bądź równe: a <= b')
    print('Większe: a > b')
    print('Większe bądź równe: a >= b')

# zadanie 4
def zadanie_4():
    liczba = int(input('podaj liczbe: '))
    if liczba >= 0:
        print('|', liczba, '| = ', liczba, sep='')
    else:
        print('|', liczba, '| = ', liczba*(-1), sep='')

# ZADANIE 5
def zadanie_5():
    a = int(input('Podaj liczbę a: '))
    b = int(input('Podaj liczbę b: '))
    c = int(input('Podaj liczbę c: '))
    if a > 0 and a <= 10:
        print('warunek a należy do (0,10> - Spełniony')
    else:
        print('warunek a należy do (0,10> - Nie spełniony')
    if a > b or b > c:
        print('warunek a > b lub b > c - Spełniony')
    else:
        print('warunek a > b lub b > c - Nie spełniony')

# ZADANIE 6
def zadanie_6():
    print('Liczby podzielne przez 5: ')
    for licznik in range (0, 1001, 5):
        print(str(licznik), end=' ')

# ZADANIE 7
def zadanie_7():
    lista = []
    for licznik in range(1, 6, 1):
        liczba = input('podaj '+str(licznik)+' liczbe: ')
        lista.append(int(liczba))
    for licznik in range(0, 5, 1):
        print(str(lista[licznik])+'^2 = '+str(lista[licznik]**2))
        
# ZADANIE 8
def zadanie_8():
    lista = []
    i = 0
    while i < 5:
        liczba = input('podaj liczbę: ')
        lista.append(int(liczba))
        i += 1
    print(lista)

# ZADANIE 9
def zadanie_9():
    liczba = int(input('Podaj liczbę wielocyfrową: '))
    suma = 0
    while(liczba != 0):
        suma = suma + liczba % 10
        liczba = liczba // 10
    print('Suma cyfr podanej liczby = '+str(suma))

# ZADANIE 10
def zadanie_10():
    for i in range(0, 6, 1):
        for j in range(0, i+1, 1):
            print('A', end='')
        print()

# ZADANIE 11
def zadanie_11():
    h = 0
    while(h < 3 or h > 9):
        print('Uwaga! Wysokość musi być nie mniejsza niż 3 i nie większa od 9!')
        h = int(input('podaj wysokość: '))
    h_parzysta = False
    if(h % 2 == 0):
        h_parzysta = True
        h = h - 1
    spacje = h // 2
    kule = 1
    for i in range (0, h // 2, 1):
        for j in range (0, spacje, 1):
            print(' ',end='')
        spacje = spacje - 1
        for j in range (0, kule, 1):
            print('O',end='')
        kule = kule + 2
        print()
    
    for i in range (0, h, 1):
        print('O', end='')
    print()
    if(h_parzysta == True):
        for i in range (0, h, 1):
            print('O', end='')
        print()
    
    spacje = 1
    kule = h - 2
    for i in range (0, h // 2, 1):
        for j in range (0, spacje, 1):
            print(' ',end='')
        spacje = spacje + 1
        for j in range (kule, 0, -1):
            print('O',end='')
        kule = kule - 2
        print()
