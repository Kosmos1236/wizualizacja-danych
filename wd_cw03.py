  
# ZADANIE 1
def zadanie_1():
    A = [1/x for x in range (1, 11, 1)]
    B = [2**x for x in range(0, 11, 1)]
    C = [x for x in B if(x % 4 == 0)]
    print(A)
    print(B)
    print(C)

# ZADANIE 2

def zadanie_2():
    macierz = [[random.randint(0, 9) for j in range (0, 4, 1)] for i in range (0, 4, 1)]
    przekatna = [macierz[i][j] for i in range (0, 4, 1) for j in range (0, 4, 1) if i == j]
    print('Macierz:')
    print(macierz[0])
    print(macierz[1])
    print(macierz[2])
    print(macierz[3])
    print('Przekątna: ',przekatna)

# ZADANIE 3
def zadanie_3():
    produkt_jednostka = {
        'mięso': 'kg',
        'chipsy': 'paczka',
        'woda': 'butelka',
    }
    jednostka_produkt = {value: key for key, value in produkt_jednostka.items()}
    print('Oryginalny słownik:')
    print(produkt_jednostka)
    print('Odwrócony słownik:')
    print(jednostka_produkt)

# ZADANIE 4
def monotonicznosc(a):
    if(a>0):
        return 'rosnąca'
    if(a<0):
        return 'malejąca'
    if(a==0):
        return 'stała'

def zadanie_4():
    print('y = ax + b')
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    print('Funkcja y = '+str(a)+'x + '+str(b)+' jest '+str(monotonicznosc(a)))

# ZADANIE 5
def proste_czy_rownolegle(a1, a2):
    if(a1 == a2):
        return 'równoległe'
    if(a1*a2 == -1):
        return 'prostopadłe'
    else:
        return 'ani równoległe ani prostopadłe'

def zadanie_5():
    print('y = ax + b')
    a1 = float(input('Podaj a1: '))
    b1 = float(input('Podaj b1: '))
    a2 = float(input('Podaj a2: '))
    b2 = float(input('Podaj b2: '))
    print('y1 = '+str(a1)+'x + '+str(b1))
    print('y2 = '+str(a2)+'x + '+str(b2))
    print('Proste y1 i y2 są '+str(proste_czy_rownolegle(a1, a2)))

# ZADANIE 6
def okrag(a = 0, b = 0, x = 0, y = 0):
    return ((x-a)**2 + (y-b)**2)**0.5

def zadanie_6():
    print('Współrzędne środka okręgu to (a,b)')
    a = input('Podaj współrzędną a: ')
    b = input('Podaj współrzędną b: ')
    print('Do okręgu należy punkt o współrzędnych (x,y)')
    x = input('Podaj współrzędną x: ')
    y = input('Podaj współrzędną y: ')
    print('Promień okręgu ma długość równą:',okrag(float(a), float(b), float(x), float(y)))

# ZADANIE 7
def pitagoras(a = 0, b = 0):
    return (a**2 + b**2)**0.5

def zadanie_7():
    a = float(input('Podaj dłguość pierwszej przyprostokątnej: '))
    b = float(input('Podaj dłguość drugiej przyprostokątnej: '))
    print('Długość przeciwprostokątnej wynosi: '+str(pitagoras(a,b)))
    
# ZADANIE 8
def ciag_suma(a1 = 1, r = 1, ile = 10):
    return ile * ((2*a1) + (ile-1)*r) / 2

def zadanie_8():
    a1 = float(input('Podaj a1: '))
    r = float(input('Podaj r: '))
    ile = int(input('Podaj ile: '))
    print('Suma = ',str(ciag_suma(a1, r, ile)))

# ZADANIE 9
def iloczyn_ciagu(* liczby):
    if(len(liczby) == 0):
        return 0.0
    else:
        iloczyn = 1.0
        for i in liczby:
            iloczyn = iloczyn * i
        return iloczyn

def zadanie_9():
    print('iloczyn dla ciągu bez elementów:', iloczyn_ciagu())
    print('iloczyn dla ciągu 1,2,3,4:', iloczyn_ciagu(1,2,3,4))
    print('iloczyn dla ciągu 1,2,3.2,4.23,5,6,7.51:', iloczyn_ciagu(1,2,3.2,4.23,5,6,7.51))

# ZADANIE 10

def ilosc_produnktow(**lista_zakupow):
    suma = 0.0
    for i in lista_zakupow:
        suma = suma + float(lista_zakupow[i])
    return suma

def zadanie_10():
    print('liczba wszystkich produktów:', ilosc_produnktow(woda_gazowana=5,chipsy=2,
          woda_mineralna=6, jabłko=6, gruszka=5))

# ZADANIE 11
def zadanie_11():
    liczba = 1+1j
    print('Liczba: '+str(liczba))
    print('Część rzeczywista: '+str(lz_postac.rzeczywista(liczba)))
    print('Część urojona: '+str(lz_postac.urojona(liczba)))
    print('Liczba1 = 1+2j, liczba2 = -23+1j')
    liczba1 = 1+2j
    liczba2 = -23+1j
    print('Liczba 1 + liczba 2 = '+str(lz_operacje.lz_dodawanie(liczba1, liczba2)))
    print('Liczba 1 - liczba 2 = '+str(lz_operacje.lz_odejmowanie(liczba1, liczba2)))
© 2020 GitHub, Inc.
