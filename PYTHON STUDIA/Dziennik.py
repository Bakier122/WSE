class Dziennik:
    def __init__(self):
        self.oceny = []
        self.uwagi = []
        self.historia = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        self.historia.append(('dodaj_ocene', ocena))
        self.pokaz_oceny()

    def usun_ocene(self, ocena):
        if ocena in self.oceny:
            self.oceny.remove(ocena)
            self.historia.append(('usun_ocene', ocena))
            self.pokaz_oceny()
        else:
            print("Ocena nie istnieje.")
            self.pokaz_oceny()

    def oblicz_srednia(self):
        if self.oceny:
            return sum(self.oceny) / len(self.oceny)
        else:
            return 0

    def dodaj_uwage(self, uwaga):
        self.uwagi.append(uwaga)
        self.historia.append(('dodaj_uwage', uwaga))

    def usun_uwage(self, uwaga):
        if uwaga in self.uwagi:
            self.uwagi.remove(uwaga)
            self.historia.append(('usun_uwage', uwaga))
        else:
            print("Uwaga nie istnieje.")

    def cofnij(self):
        if self.historia:
            ostatnia_akcja, wartosc = self.historia.pop()
            if ostatnia_akcja == 'dodaj_ocene':
                self.oceny.remove(wartosc)
            elif ostatnia_akcja == 'usun_ocene':
                self.oceny.append(wartosc)
            elif ostatnia_akcja == 'dodaj_uwage':
                self.uwagi.remove(wartosc)
            elif ostatnia_akcja == 'usun_uwage':
                self.uwagi.append(wartosc)
        else:
            print("Brak historii do cofnięcia.")

    def pokaz_oceny(self):
        print("Oceny:", self.oceny)
        print("Średnia ocen:", self.oblicz_srednia())
        input("Naciśnij Enter, aby wrócić do menu...")

    def pokaz_ucznia(self):
        print("Oceny:", self.oceny)
        print("Uwagi:", self.uwagi)
        print("Średnia ocen:", self.oblicz_srednia())

    def wyjdz(self):
        print("Wyjście z programu.")
        exit()


def menu():
    dziennik = Dziennik()
    while True:
        print("\n--- Dziennik ---")
        print("1. Dodaj ocenę")
        print("2. Usuń ocenę")
        print("3. Oblicz średnią")
        print("4. Dodaj uwagę")
        print("5. Usuń uwagę")
        print("6. Cofnij")
        print("7. Pokaż ucznia")
        print("8. Wyjdź")
        
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            ocena = float(input("Podaj ocenę: "))
            dziennik.dodaj_ocene(ocena)
        elif wybor == '2':
            ocena = float(input("Podaj ocenę do usunięcia: "))
            dziennik.usun_ocene(ocena)
        elif wybor == '3':
            print("Średnia ocen:", dziennik.oblicz_srednia())
            input("Naciśnij Enter, aby wrócić do menu...")
        elif wybor == '4':
            uwaga = input("Podaj uwagę: ")
            dziennik.dodaj_uwage(uwaga)
        elif wybor == '5':
            uwaga = input("Podaj uwagę do usunięcia: ")
            dziennik.usun_uwage(uwaga)
        elif wybor == '6':
            dziennik.cofnij()
        elif wybor == '7':
            dziennik.pokaz_ucznia()
            input("Naciśnij Enter, aby wrócić do menu...")
        elif wybor == '8':
            dziennik.wyjdz()
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")

if __name__ == "__main__":
    menu()
