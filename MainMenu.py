from Communication import *

def menu():
    while True:
        print("Da li zelite da pisete ili da citate?")
        x= input()
        if x=="w":
            connectToWriter()
        elif x=="r":
            connectToReader()
        elif x=="x":
            break
