from wymierna import Wymierna

def main():
    w1 = Wymierna(5, 8)
    w2 = Wymierna(7)
    w3 = Wymierna()
    w4 = Wymierna(12, -2)

    print('w1 = ', w1, '\nw2 = ', w2, '\nw3 = ', w3, '\nw4 = ', w4, '\nLicznik liczby ', w1, ' to ', w1.l(),
          ', natomiast jej mianownik to ', w1.m(), '\n', Wymierna(5, 3), ' + ', Wymierna(3, 12), ' = ',
          Wymierna(5,3) + Wymierna(3, 12), '\n', Wymierna(5,3), ' * ', Wymierna(3, 12), ' = ',
          Wymierna(5, 3) * Wymierna(3, 12), '\n')

    print('*********czesc ambitniejsza:*********\n')


    v_w5 = input('w5 = ') # bierze to jako string, po czym zmienia w int
    w5 = Wymierna()
    w5.set_stoi(v_w5)
    print('zapisane: w5 = ', w5)

    w6 = Wymierna()
    v_w6 = input('w6 = ')
    w6.set_stoi(v_w6)
    print('zapisane: w6 = ', w6)


    A = [Wymierna(3, 5), Wymierna(5, 6), Wymierna(-2, 5), Wymierna(5, 12)]

    print('************************')

    for i in A:
        print(i, end=' ')

    print('\n************************')

    A.sort() # sortowanie listy A

    print('************************')

    for i in A:
        print(i, end=' ')

    print('\n************************')


    S = {Wymierna(4, 5), Wymierna(-8, 2), Wymierna(16, -4)} # set

    for i in S:
        print(i, end=' ')

    print('\n')


    T = {Wymierna(4, 5), -4}

    if T == S:
        print('zbiory identyczne')
    else:
        print('zbiory nie sa identyczne')


    V = {Wymierna(4,5), -4, 5}

    if V < T:
        print('V zawarty w T\n')
    if T < V:
        print('T zawarty w V\n')


    x = Wymierna(4,5)

    if x in T:
        print('liczba ', x, ' jest w tym zbiorze\n')
    else:
        print('liczby ', x, ' nie ma w tym zbiorze\n')

    y = Wymierna(7, 15)

    if y in T:
        print('liczba ', y, ' jest w tym zbiorze\n')
    else:
        print('liczby ', y, ' nie ma w tym zbiorze\n')

if __name__ == "__main__":
    main()
