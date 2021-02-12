def register_page():
    import PySimpleGUI as sg
    sg.theme('DarkPurple4')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Cayman Islands National Bank™', size=(30, 1), font='Courier 20')],
              [sg.Text('Name   '), sg.InputText()],
              [sg.Text('Password   '), sg.InputText(key='Password', password_char='*')],
              [sg.Text('Mail adress'), sg.InputText()],
              [sg.Button('Register'), sg.Button('Back'), sg.Button('Cancel')]]

    window = sg.Window('Cayman Islands National Bank™', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Back':
            login_page()
            break
        if event == 'Register':
            print('Welcome to Cayman Islands National Bank™')
            #save registrstion info
            pass

    window.close()