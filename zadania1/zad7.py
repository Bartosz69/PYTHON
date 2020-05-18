while True:

    print("Podaj liczbe: ")
    liczba = input()
    liczba = int(liczba)
    a = liczba*liczba
    print("potega z liczby", liczba, "wynosi: ", a)

    b = input()

    if b == 'n':
        print("Koniec pracy Programu")
        break
