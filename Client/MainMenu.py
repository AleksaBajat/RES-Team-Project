from ReaderConnection import *
from WriterConnection import *


def menu():
    while True:
        print("Da li zelite da pisete ili da citate? Unesite slovo w za pisanje ili slovo r za citanje")
        x = input()
        if x == "w":
            connect_to_writer()
        elif x == "r":
            print(
                "Odaberite opciju citanja\n" + 
                "1 - Procitaj sve\n" + 
                "2 - Procitaj po odredjenom mesecu\n" +
                "3 - Procitaj po korisniku\n" + 
                "4 - Procitaj po gradu" +
                "5 - Procitaj po potrosnji vecoj od..." +
                "6 - Procitaj po potrosnji manjoj od...")
            y = input()
            z = '0'
            if y == "2":
                print("Unesite redni broj meseca u godini")
                z = input()
            elif y == "3":
                print("Unesite id korisnika")
                z = input()
            elif y == "4":
                print("Unesite grad")
                z = input()
            elif y == "5":
                print("Unesite vrednost potrosnje")
                z = input()
            elif y == "6":
                print("Unesite vrednost potrosnje")
                z = input()
            connectToReader(y, z)
        elif x == "x":
            break
