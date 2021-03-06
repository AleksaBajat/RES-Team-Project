from ReaderConnection import connect_to_reader
from WriterConnection import connect_to_writer


def menu():
    print("Welcome to the Cache Memory System. Here you can manipulate meter readings.")
    while True:
        print("Insert (without quotes) 'w' to write or 'r' to read 'x' to exit!")
        x = input()
        if x == "w":
            connect_to_writer()
        elif x == "r":
            print(
                "Pick an option ('without quotes, just a number')\n" +
                "1 - Read All\n" +
                "2 - Read by Month\n" +
                "3 - Read by User\n" +
                "4 - Read by City\n" +
                "5 - Read by consumption more than...\n" +
                "6 - Read by consumption less than...\n")
            option = input()
            parameter = '0'
            if option == "2":
                print("Insert month:")
                parameter = input().capitalize()
            elif option == "3":
                print("Insert user id:")
                parameter = input()
            elif option == "4":
                print("Insert city:")
                parameter = input()
            elif option == "5" or option == "6":
                print("Insert consumption:")
                parameter = input()
            connect_to_reader(option, parameter)
        elif x == "x":
            break
