# ZADANIE1
def zadanie_1():
    int_1 = 16
    int_2 = 145
    float_1, float_2 = 3.001, -2.31
    complex_1 = 8 + 1j
    complex_2 = 4 - 3j
    string_1 = 'Ala ma kotka'
    string_2 = 'kotek'
    print('int: ', int_1, int_2)
    print('float: ', float_1, float_2)
    print('complex: ', complex_1, complex_2)
    print('string: ', string_1, string_2)

# ZADANIE 2
def zadanie_2():
    a=10
    b=5
    print('Dodawanie:', a, '+', b, '=', a+b)
    print('Odejmowanie:', a, '-', b, '=', a-b)
    print('Mnożenie:', a, '*', b, '=', a*b)
    print('Dzielenie:', a, '/', b, '=', a/b)
    print('Dzielenie calkowite:', a, '//', b, '=', a//b)
    print('Reszta z dzielenia:', a, '%', b, '=', a%b)
    print('Potegowanie:', a, 'do potegi', b, '=', a**b)
    print('Potegowanie:', b, 'do potegi', a, '=', pow(b,a))

# ZADANIE 3
def zadanie_3():
    print('a = 3')
    a = 3
    a += 5
    print('a += 5:', a)
    a = 3
    a -= 5
    print('a -= 5:', a)
    a = 3
    a *= 5
    print('a *= 5:', a)
    a = 3
    a /= 5
    print('a /= 5:', a)
    a = 3
    a **= 5
    print('a **= 5:', a)
    a = 3
    a %= 5
    print('a %= 5:', a)

# ZADANIE 4
from math import *

def zadanie_4():
    print('e do potegi 10 = ', pow(e, 10))
    print('(ln(5+sin^2(8)))^(1/6) = ', pow( log(5 + pow(sin(8), 2)), 1/6))
    print('⌊3,55⌋ = ', floor(3.55))
    print('⌈4,80⌉ = ', ceil(4.80))

# ZADANIE 5
def zadanie_5():
    imie = 'Karolina'
    nazwisko = 'Maliszewska'
    print(str.capitalize(imie), str.capitalize(nazwisko))

# ZADANIE 6
def zadanie_6():
    piosenka = 'la la la la la la la la la la la la la la la la la la la la'
    print('"la" powtarza sie', piosenka.count('la'), 'razy')

# ZADANIE 7
def zadanie_7():
    napis = 'krotki tekst'
    print('napis =', napis)
    print('napis[1] =', napis[1])
    print('napis[1] =', napis[-1])

# ZADANIE 8
def zadanie_8():
    piosenka = 'la la la la la la la la la la la la la la la la la la la la'
    print(str.split(piosenka))

# ZADANIE 9
def zadanie_9():
    z_string = 'tekst'
    z_float = 342
    z_hexdec = hex(255)
    print('string: %(zm)s' % {'zm': z_string})
    print('float: %(zm)f' % {'zm': z_float})
    print('szestnastkowe: %(zm)s' % {'zm': z_hexdec})

# ZADANIE 10
def zadanie_10():
    filmy = [
        'Titanic',
        'Jak wytresować smoka', 'Trzy metry nad niebem',
        'Planeta małp', 'Need for speed'
    ]
    print('Lista filmów przed posortowaniem:\n', filmy)
    filmy.sort()
    print('Lista filmów po posortowaniu:\n', filmy)

# ZADANIE 11
def zadanie_11():
    tabelka = [
        ['kat', '0', '30', '45', '60', '90'],
        ['sin', sin(0), sin(30), sin(45), sin(60), sin(90)],
        ['cos', cos(0), cos(30), cos(45), cos(60), cos(90)],
        ['tan', tan(0), tan(30), tan(45), tan(60), tan(90)]
    ]
    print(tabelka[0])
    print(tabelka[1])
    print(tabelka[2])
    print(tabelka[3])

# ZADANIE 12
def zadanie_12():
    napis = 'Ala ma kotka a Beata ma pieska'
    lista_slow = str.split(napis)
    print(napis)
    print(lista_slow)

# ZADANIE 13
def zadanie_13():
    znajomi = {
        'Miko': ['Mikołaj', 'Nowak],
        'Anka': ['Anna', 'Kotecka'],
        'Smerf': ['Szymon', 'Kowalski']
        'Lizak': ['Artur','Lizak']
        'Szymi': ['Szymon','Figula']
        'Dzik': ['Robert','Dzik']
        'Mario': ['Mariusz','Nowak']
        'Pablo': ['Paweł', 'Turek']
        'Antek': ['Jakub','Antkiewicz']
        'Monia': ['Monika',"Maj"]
    }
    print(znajomi['Miko'])
    print(znajomi['Mario'])
    print(znajomi['Antek'])
    
