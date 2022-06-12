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
            option = input()
            parameter = '0'
            if option == "2":
                print("Unesite redni broj meseca u godini")
                parameter = input()
            elif option == "3":
                print("Unesite id korisnika")
                parameter = input()
            elif option == "4":
                print("Unesite grad")
                parameter = input()
            elif option == "5":
                print("Unesite vrednost potrosnje")
                parameter = input()
            elif option == "6":
                print("Unesite vrednost potrosnje")
                parameter = input()
            connect_to_reader(option, parameter)
        elif x == "x":
            break
