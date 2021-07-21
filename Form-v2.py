# Libs
import PySimpleGUI as sg
from time import sleep


# Start
def FormPy():
    sg.theme("DarkTeal7")
    layout = [
        [sg.Text("First Name |", text_color="black", size=(9, 0)), sg.Input(key="firstname", size=(20, 0), border_width=3, justification="center")],
        [sg.Text("Last Name |", text_color="black", size=(9, 0)), sg.Input(key="lastname", size=(20, 0), border_width=3,justification="center")],
        [sg.Text("Age |", text_color="black", size=(9, 0)), sg.Input(key="age", size=(8, 0), border_width=3, justification="center")],

        [sg.Text("-" * 66)],
        
        [sg.Text("Identity |", text_color="black", size=(9, 0)), sg.Input(key="identity", size=(20, 0), border_width=3, justification="center")],
        [sg.Text("License |", text_color="black", size=(9, 0)), sg.Input(key="license", size=(20, ), border_width=3, justification="center")],

        [sg.Text("-" * 66)],

        [sg.Text("Email |", text_color="black", size=(9, 0)), sg.Input(key="email", size=(25, 0), border_width=3, justification="center")],
        [sg.Text("Number |", text_color="black", size=(9, 0)), sg.Input(key="number", size=(15, 0), border_width=3, justification="center")],
        
        [sg.Text("-" * 66)],

        [sg.Text(" " * 23), sg.Button("Register", size=(6, 0))],

        [sg.Text("-" * 66)],

        [sg.Output(size=(35, 5))],
        
        [sg.Text(" " * 18), sg.Text("(c) NT Developer", text_color="black",)]
    ]

    return sg.Window("FormPy", layout=layout)

windows = FormPy()

while True:
    try:
        event, values = windows.Read()

        # Close windows
        if event == sg.WINDOW_CLOSED:
            break

        # Dates
        firstname = str(values["firstname"]).capitalize()
        lastname = str(values["lastname"]).capitalize()
        age = int(values["age"])

        identity = str(values["identity"])
        license = str(values["license"])

        email = str(values["email"])
        number = int(values["number"])


        # Register
        def Register():
            if event == "Register":
                code = 0
                code += 1
                
                print("-" * 60)

                print("                  - REGISTERED! -")
                print(f"NameCode - #{code}_#{firstname}{lastname}")

                print("-" * 60)
                print(" ")

        # Defs
        Register()

    except Exception as error:
        print("-" * 60)
        
        print("                       - ERROR! -")
        print(f"ErrorCode - {error}")

        print("-" * 60)
        print(" ")

