import sqlite3

polaczenie = sqlite3.connect("MenadzerZadań.db")


def stwoz_tabele(polaczenie):
    try:
        kursor = polaczenie.cursor()
        kursor.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def pokaz_zadania(polaczenie):
    kursor = polaczenie.cursor()
    kursor.execute("""SELECT rowid, task FROM task""")
    rezultat = kursor.fetchall()

    for wiersz in rezultat:
        print(f"{wiersz[0]} - {wiersz[1]}")

def dodanie_zadania(polaczenie):
    dodaje = input("Wpisz zadanie które chcesz dodać: ")
    if dodaje == "0":
        print("Powrót do menu")
    else:
        kursor = polaczenie.cursor()
        kursor.execute("""INSERT INTO task(task) VALUES(?)""",(dodaje,))
        polaczenie.commit()
        print("Dodano zadanie")


def usuwanie_zadania(polaczenie):
    usuwam = int(input("Podaj numer zadania: "))
    kursor = polaczenie.cursor()
    usuniete = kursor.execute("""DELETE FROM task WHERE rowid=?""", (usuwam,)).rowcount
    polaczenie.commit()

    if usuniete == 0:
        print("Takie zadanie nie istnieje")
    else:
        print("Usunięto zadanie")


stwoz_tabele(polaczenie)

while True:
    print("(1) Pokaż zadania")
    print("(2) Dodaj zadanie")
    print("(3) Usuń zadanie")
    print("(4) Wyjdź")

    wybor = input("Wybierz czynność(1-4): ")

    try:
        wybor = int(wybor)
        if wybor == 1:
            pokaz_zadania(polaczenie)
            print()
        elif wybor == 2:
            dodanie_zadania(polaczenie)
            print()
        elif wybor == 3:
            usuwanie_zadania(polaczenie)
            print()
        elif wybor == 4:
            print("Dziękujemy za korzystanie z programu!")
            break
        else:
            print("Wybrana wartość nie jest liczbą z przedziału (1-4)")
    except ValueError:
        print("Wybrana wartość nie jest liczbą z przedziału (1-4)")

polaczenie.close()