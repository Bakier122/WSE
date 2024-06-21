class Dziennik:  # Definiowanie klasy o nazwie Dziennik
    def __init__(self):  # Metoda inicjalizująca dla klasy
        self.oceny = []  # Lista do przechowywania ocen
        self.uwagi = []  # Lista do przechowywania uwag
        self.historia = []  # Lista do przechowywania historii akcji

    def dodaj_ocene(self, ocena):  # Metoda dodająca ocenę
        self.oceny.append(ocena)  # Dodanie oceny do listy
        self.historia.append(('dodaj_ocene', ocena))  # Zapisanie akcji do historii
        self.pokaz_oceny()  # Wyświetlenie aktualnych ocen

    def usun_ocene(self, ocena):  # Metoda usuwająca ocenę
        if ocena in self.oceny:  # Sprawdzenie, czy ocena istnieje w liście
            self.oceny.remove(ocena)  # Usunięcie oceny z listy
            self.historia.append(('usun_ocene', ocena))  # Zapisanie akcji do historii
            self.pokaz_oceny()  # Wyświetlenie aktualnych ocen
        else:
            print("Ocena nie istnieje.")  # Wyświetlenie komunikatu, jeśli ocena nie istnieje
            self.pokaz_oceny()  # Wyświetlenie aktualnych ocen

    def oblicz_srednia(self):  # Metoda obliczająca średnią ocen
        if self.oceny:  # Sprawdzenie, czy istnieją jakieś oceny
            return sum(self.oceny) / len(self.oceny)  # Obliczenie średniej ocen
        else:
            return 0  # Zwrócenie 0, jeśli brak ocen

    def dodaj_uwage(self, uwaga):  # Metoda dodająca uwagę
        self.uwagi.append(uwaga)  # Dodanie uwagi do listy
        self.historia.append(('dodaj_uwage', uwaga))  # Zapisanie akcji do historii

    def usun_uwage(self, uwaga):  # Metoda usuwająca uwagę
        if uwaga in self.uwagi:  # Sprawdzenie, czy uwaga istnieje w liście
            self.uwagi.remove(uwaga)  # Usunięcie uwagi z listy
            self.historia.append(('usun_uwage', uwaga))  # Zapisanie akcji do historii
        else:
            print("Uwaga nie istnieje.")  # Wyświetlenie komunikatu, jeśli uwaga nie istnieje

    def cofnij(self):  # Metoda cofająca ostatnią akcję
        if self.historia:  # Sprawdzenie, czy istnieje jakaś historia
            ostatnia_akcja, wartosc = self.historia.pop()  # Pobranie ostatniej akcji i wartości
            if ostatnia_akcja == 'dodaj_ocene':  # Cofnięcie dodania oceny
                self.oceny.remove(wartosc)
            elif ostatnia_akcja == 'usun_ocene':  # Cofnięcie usunięcia oceny
                self.oceny.append(wartosc)
            elif ostatnia_akcja == 'dodaj_uwage':  # Cofnięcie dodania uwagi
                self.uwagi.remove(wartosc)
            elif ostatnia_akcja == 'usun_uwage':  # Cofnięcie usunięcia uwagi
                self.uwagi.append(wartosc)
        else:
            print("Brak historii do cofnięcia.")  # Wyświetlenie komunikatu, jeśli brak historii do cofnięcia

    def pokaz_oceny(self):  # Metoda wyświetlająca oceny
        print("Oceny:", self.oceny)  # Wyświetlenie listy ocen
        print("Średnia ocen:", self.oblicz_srednia())  # Wyświetlenie średniej ocen
        input("Naciśnij Enter, aby wrócić do menu...")  # Oczekiwanie na naciśnięcie Enter

    def pokaz_ucznia(self):  # Metoda wyświetlająca dane ucznia
        print("Oceny:", self.oceny)  # Wyświetlenie listy ocen
        print("Uwagi:", self.uwagi)  # Wyświetlenie listy uwag
        print("Średnia ocen:", self.oblicz_srednia())  # Wyświetlenie średniej ocen

    def wyjdz(self):  # Metoda wychodząca z programu
        print("Wyjście z programu.")  # Wyświetlenie komunikatu o wyjściu
        exit()  # Zakończenie programu


def menu():  # Funkcja obsługująca menu
    dziennik = Dziennik()  # Utworzenie obiektu klasy Dziennik
    while True:  # Pętla nieskończona
        print("\n--- Dziennik ---")
        print("1. Dodaj ocenę")
        print("2. Usuń ocenę")
        print("3. Oblicz średnią")
        print("4. Dodaj uwagę")
        print("5. Usuń uwagę")
        print("6. Cofnij")
        print("7. Pokaż ucznia")
        print("8. Wyjdź")
        
        wybor = input("Wybierz opcję: ")  # Pobranie wyboru użytkownika

        if wybor == '1':  # Opcja dodania oceny
            ocena = float(input("Podaj ocenę: "))  # Pobranie oceny od użytkownika
            dziennik.dodaj_ocene(ocena)  # Dodanie oceny do dziennika
        elif wybor == '2':  # Opcja usunięcia oceny
            ocena = float(input("Podaj ocenę do usunięcia: "))  # Pobranie oceny do usunięcia od użytkownika
            dziennik.usun_ocene(ocena)  # Usunięcie oceny z dziennika
        elif wybor == '3':  # Opcja obliczenia średniej
            print("Średnia ocen:", dziennik.oblicz_srednia())  # Wyświetlenie średniej ocen
            input("Naciśnij Enter, aby wrócić do menu...")  # Oczekiwanie na naciśnięcie Enter
        elif wybor == '4':  # Opcja dodania uwagi
            uwaga = input("Podaj uwagę: ")  # Pobranie uwagi od użytkownika
            dziennik.dodaj_uwage(uwaga)  # Dodanie uwagi do dziennika
        elif wybor == '5':  # Opcja usunięcia uwagi
            uwaga = input("Podaj uwagę do usunięcia: ")  # Pobranie uwagi do usunięcia od użytkownika
            dziennik.usun_uwage(uwaga)  # Usunięcie uwagi z dziennika
        elif wybor == '6':  # Opcja cofnięcia ostatniej akcji
            dziennik.cofnij()  # Cofnięcie ostatniej akcji w dzienniku
        elif wybor == '7':  # Opcja wyświetlenia danych ucznia
            dziennik.pokaz_ucznia()  # Wyświetlenie danych ucznia
            input("Naciśnij Enter, aby wrócić do menu...")  # Oczekiwanie na naciśnięcie Enter
        elif wybor == '8':  # Opcja wyjścia z programu
            dziennik.wyjdz()  # Wyjście z programu
        else:
            print("Niepoprawna opcja, spróbuj ponownie.")  # Wyświetlenie komunikatu o niepoprawnej opcji

if __name__ == "__main__":  # Blok sprawdzający, czy skrypt jest uruchamiany bezpośrednio
    menu()  # Wywołanie funkcji menu
