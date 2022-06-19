from ReaderConnection import connect_to_reader
from WriterConnection import connect_to_writer


def menu():
    print("Welcome to the Cache Memory System. Here you can manipulate meter readings.")
    while True:
        print("Insert (without quotes) 'w' to write or 'r' to read!")
        x = input()
        if x == "w":
            connect_to_writer()
        elif x == "r":
            print(
                "Pick an option ('without quotes, just a number')\n" +
                "1 - Read All\n" +
                "2 - Read by Month\n" +
                "3 - Read by User\n" +
                "4 - Read by City" +
                "5 - Read by consumption more than..." +
                "6 - Read by consumption less than...")
            option = input()
            parameter = '0'
            if option == "2":
                print("Insert months ordinal number!")
                print("1 - January")
                print("2 - February")
                print("3 - March")
                print("4 - April")
                print("5 - May")
                print("6 - June")
                print("7 - July")
                print("8 - August")
                print("9 - September")
                print("10 - October")
                print("11 - November")
                print("12 - December")
                parameter = input()
            elif option == "3":
                print("Insert user id!")
                parameter = input()
            elif option == "4":
                print("Insert city!")
                parameter = input()
            elif option == "5" or option == "6":
                print("Insert consumptions!")
                parameter = input()
            connect_to_reader(option, parameter)
        elif x == "x":
            break
