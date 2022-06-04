from readerConnection import *
from wirterConnection import *


def menu():
    while True:
        print("Da li zelite da pisete ili da citate? Unesite slovo w za pisanje ili slovo r za citanje")
        x = input()
        if x == "w":
            connectToWriter()
        elif x == "r":
            print(
                "Odaberite opciju citanja\n1 - Procitaj sve\n2 - Procitaj po odredjenom mesecu\n3 - Procitaj po korisniku\n4 - Procitaj po gradu")
            y = input()
            z = 0
            if y == "2":
                print("Unesite redni broj meseca u godini")
                z = input()
            elif y == "3":
                print("Unesite id korisnika")
                z = input()
            elif y == "4":
                print("Unesite grad")
                z = input()
            connectToReader(y, z)
        elif x == "x":
            break
