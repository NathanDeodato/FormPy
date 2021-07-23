# Libs
from os import system
from time import sleep


# Start
def FormPy():
    try:
        print("-" * 50)
        print("- FormPy -".center(50))
        print("-" * 50)
        
        Firstname = str(input("Firstname - ")).capitalize()
        Lastname = str(input("Lastname - ")).capitalize()

        print("----".center(50))
        sleep(0.6)

        Country = str(input("Country - ")).lower()

        State = str(input("State - ")).capitalize()

        print("----".center(50))
        sleep(0.6)

        Identity = str(input("Identity - "))
        License = str(input("License - "))

        print("----".center(50))
        sleep(0.6)

        Email = str(input("Email - "))

        Number = int(input("Number - "))
        while type(Number) != int:
            print("-" * 50)
            print("CodeError - Number invalid.")
            print("-" * 50)

            sleep(0.6)

            Number = int(input("Number - "))
            if type(Number) == int:
                break

        print("----".center(50))
        sleep(0.6)

        def Register():
            code = 0
            code += 1

            sleep(0.6)
            print("")
            print(f"NameCode - #{code}_#{Firstname}{Lastname}")
        Register()

    except Exception as error:
        print("-" * 50)
        sleep(0.6)

        print("- ERROR! -".center(50))
        print(f"CodeError - {error}")
        
        sleep(0.6)


# Loop FormPy
while True:
    print("-" * 50)
    next = str(input("Register - [S/n]")).lower()
    
    system("cls")
    sleep(1)

    if next == "s":
        FormPy()
    else:
        print("-" * 50)

        sleep(0.6)
        print("(c) NT Developer".center(50))

        print("-" * 50)
        break
