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
        
        Age = int(input("Age - "))
        while type(Age) != int:
            print("-" * 50)
            print("CodeError - Age invalid.")
            print("-" * 50)
            
            Age = int(input("Age - "))

        print("----".center(50))
        sleep(0.6)

        Identity = str(input("Identity - "))
        License = str(input("License - "))

        print("----".center(50))
        sleep(0.6)

        Email = str(input("Email - "))
        while not "@" and ".com" in Email:
            print("-" * 50)
            print("CodeError - Email invalid.")
            print("-" * 50)

            Email = str(input("Email - "))

        Number = int(input("Number - "))
        while type(Number) != int:
            print("-" * 50)
            print("CodeError - Number invalid.")
            print("-" * 50)
            
            Number = int(input("Number - "))

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
        print("-" * 50)

# Defs
FormPy()

print("-" * 50)

sleep(0.6)
print("(c) NT Developer".center(50))

print("-" * 50)
