import PySimpleGUI as sg

#import för färg på texten
from colorama import init
from colorama import Fore, Back, Style
init()


print(Fore.GREEN + "Cayman Islands National Bank™")

sg.theme('DarkPurple4')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Your Cayman Islands National Bank™ account')],
            [sg.Text('Current Balance: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Cayman Islands National Bank™', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()