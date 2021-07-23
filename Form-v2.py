# Libs
import PySimpleGUI as sg
from time import sleep


# Start
def FormPy():
    sg.theme("DarkTeal7")
    layout = [
        [sg.Text("First Name |", text_color="black", size=(9, 0)), sg.Input(key="firstname", size=(20, 0), border_width=3, justification="center"), sg.Text("|"), sg.Text("Country |", text_color="black", size=(7, 0)), sg.Input(key="country", size=(15, 0), border_width=3,justification="center")],
        [sg.Text("Last Name |", text_color="black", size=(9, 0)), sg.Input(key="lastname", size=(20, 0), border_width=3,justification="center"), sg.Text("|"), sg.Text("State |", text_color="black", size=(7, 0)), sg.Input(key="state", size=(15, 0), border_width=3,justification="center")],
        
        [sg.Text("-" * 111)],

        [sg.Text("Identity |", text_color="black", size=(9, 0)), sg.Input(key="identity", size=(20, 0), border_width=3, justification="center"), sg.Text("|"), sg.Text("Email |", text_color="black", size=(7, 0)), sg.Input(key="email", size=(15, 0), border_width=3, justification="center")],
        [sg.Text("License |", text_color="black", size=(9, 0)), sg.Input(key="license", size=(20, ), border_width=3, justification="center"), sg.Text("|"), sg.Text("Number |", text_color="black", size=(7, 0)), sg.Input(key="number", size=(15, 0), border_width=3, justification="center")],
        
        [sg.Text("-" * 111)],

        [sg.Text(" " * 46), sg.Button("Register", size=(6, 0))],

        [sg.Text("-" * 111)],

        [sg.Output(size=(61, 6))],
        
        [sg.Text(" " * 42), sg.Text("(c) NT Developer", text_color="black",)]
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
        
        country = str(values["country"]).capitalize()
        state = str(values["state"]).capitalize()

        identity = str(values["identity"])
        license = str(values["license"])

        email = str(values["email"])
        number = int(values["number"])


        # Register
        def Register():
            if event == "Register":
                code = 0
                code += 1
                
                print("-" * 106)
                sleep(1.5)

                print("                                             - REGISTERED! -")
                print(f"                                    NameCode - #{code}_#{firstname}{lastname}")

                print("-" * 106)
                print(" ")

        # Defs
        Register()

    except Exception as error:
        print("-" * 60)
        
        print("                       - ERROR! -")
        print(f"ErrorCode - {error}")

        print("-" * 60)
        print(" ")

