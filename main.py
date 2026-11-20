
class Uczen:
    def __init__(self, imie_nazwisko, klasa):
        self.imie_nazwisko = imie_nazwisko
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, imie_nazwisko, przedmiot, klasy):
        self.imie_nazwisko = imie_nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy


class Wychowawca:
    def __init__(self, imie_nazwisko, klasa):
        self.imie_nazwisko = imie_nazwisko
        self.klasa = klasa


def pokaz_uczniow_klasy(uczniowie, klasa):
    znaleziono = False
    for uczen in uczniowie:
        if uczen.klasa == klasa:
            print(uczen.imie_nazwisko)
            znaleziono = True
    if not znaleziono:
        print("Brak uczniów w tej klasie.")


def tworzenie(uczniowie, nauczyciele, wychowawcy):
    while True:
        print("\nTworzenie: uczeń, nauczyciel, wychowawca, koniec")
        komenda = input("Podaj komendę: ").strip().lower()

        if komenda == "uczeń" or komenda == "uczen":
            imie_nazwisko = input("Imię i nazwisko ucznia: ").strip()
            klasa = input("Klasa: ").strip().upper()
            if imie_nazwisko and klasa:
                uczniowie.append(Uczen(imie_nazwisko, klasa))
                print("Dodano ucznia.")
            else:
                print("Imię i nazwisko oraz klasa nie mogą być puste.")

        elif komenda == "nauczyciel":
            imie_nazwisko = input("Imię i nazwisko nauczyciela: ").strip()
            przedmiot = input("Przedmiot: ").strip()
            klasy = []
            print("Podawaj klasy, każdą w nowej linii. Enter kończy.")
            while True:
                klasa = input("Klasa: ").strip().upper()
                if not klasa:
                    break
                if klasa not in klasy:
                    klasy.append(klasa)

            if imie_nazwisko and przedmiot:
                nauczyciele.append(Nauczyciel(imie_nazwisko, przedmiot, klasy))
                print("Dodano nauczyciela.")
            else:
                print("Imię i nazwisko oraz przedmiot nie mogą być puste.")

        elif komenda == "wychowawca":
            imie_nazwisko = input("Imię i nazwisko wychowawcy: ").strip()
            klasa = input("Prowadzona klasa: ").strip().upper()
            zajeta = False
            for wychowawca in wychowawcy:
                if wychowawca.klasa == klasa:
                    zajeta = True

            if not imie_nazwisko or not klasa:
                print("Imię i nazwisko oraz klasa nie mogą być puste.")
            elif zajeta:
                print("Ta klasa ma już wychowawcę.")
            else:
                wychowawcy.append(Wychowawca(imie_nazwisko, klasa))
                print("Dodano wychowawcę.")

        elif komenda == "koniec":
            break

        else:
            print("Nieznana komenda.")


def zarzadzanie(uczniowie, nauczyciele, wychowawcy):
    while True:
        print("\nZarządzanie: klasa, uczeń, nauczyciel, wychowawca, koniec")
        komenda = input("Podaj komendę: ").strip().lower()

        if komenda == "klasa":
            klasa = input("Podaj klasę: ").strip().upper()
            if not klasa:
                print("Nazwa klasy nie może być pusta.")
                continue
            print("Uczniowie klasy {}:".format(klasa))
            pokaz_uczniow_klasy(uczniowie, klasa)
            znaleziono = False
            for wychowawca in wychowawcy:
                if wychowawca.klasa == klasa:
                    print("Wychowawca: {}".format(wychowawca.imie_nazwisko))
                    znaleziono = True
            if not znaleziono:
                print("Brak wychowawcy tej klasy.")

        elif komenda == "uczeń" or komenda == "uczen":
            imie_nazwisko = input("Imię i nazwisko ucznia: ").strip()
            znaleziono = False
            for uczen in uczniowie:
                if uczen.imie_nazwisko.lower() == imie_nazwisko.lower():
                    znaleziono = True
                    print("Uczeń: {}, klasa {}".format(
                        uczen.imie_nazwisko, uczen.klasa
                    ))
                    ma_lekcje = False
                    for nauczyciel in nauczyciele:
                        if uczen.klasa in nauczyciel.klasy:
                            print("{}: {}".format(
                                nauczyciel.przedmiot, nauczyciel.imie_nazwisko
                            ))
                            ma_lekcje = True
                    if not ma_lekcje:
                        print("Brak przypisanych lekcji.")
            if not znaleziono:
                print("Nie znaleziono ucznia.")

        elif komenda == "nauczyciel":
            imie_nazwisko = input("Imię i nazwisko nauczyciela: ").strip()
            znaleziono = False
            for nauczyciel in nauczyciele:
                if nauczyciel.imie_nazwisko.lower() == imie_nazwisko.lower():
                    znaleziono = True
                    print("Przedmiot: {}".format(nauczyciel.przedmiot))
                    if nauczyciel.klasy:
                        for klasa in nauczyciel.klasy:
                            print("Klasa: {}".format(klasa))
                    else:
                        print("Brak przypisanych klas.")
            if not znaleziono:
                print("Nie znaleziono nauczyciela.")

        elif komenda == "wychowawca":
            imie_nazwisko = input("Imię i nazwisko wychowawcy: ").strip()
            znaleziono = False
            for wychowawca in wychowawcy:
                if wychowawca.imie_nazwisko.lower() == imie_nazwisko.lower():
                    znaleziono = True
                    print("Uczniowie klasy {}:".format(wychowawca.klasa))
                    pokaz_uczniow_klasy(uczniowie, wychowawca.klasa)
            if not znaleziono:
                print("Nie znaleziono wychowawcy.")

        elif komenda == "koniec":
            break

        else:
            print("Nieznana komenda.")


uczniowie = []
nauczyciele = []
wychowawcy = []

while True:
    print("\nMenu główne: utwórz, zarządzaj, koniec")
    komenda = input("Podaj komendę: ").strip().lower()

    if komenda == "utwórz" or komenda == "utworz":
        tworzenie(uczniowie, nauczyciele, wychowawcy)
    elif komenda == "zarządzaj" or komenda == "zarzadzaj":
        zarzadzanie(uczniowie, nauczyciele, wychowawcy)
    elif komenda == "koniec":
        print("Koniec programu.")
        break
    else:
        print("Nieznana komenda.")
