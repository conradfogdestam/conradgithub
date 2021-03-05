def login_page():

    import PySimpleGUI as sg
    from bankappregister import register_page

    sg.theme('DarkPurple4')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Cayman Islands National Bank™', size=(30, 1), font='Courier 20')],
                [sg.Text('Name'), sg.InputText(key='-IN-0')],
                [sg.Text('Password'), sg.InputText(key='-IN-1', password_char='*')],
                [sg.Button('Login'), sg.Button('Register'), sg.Button('Cancel')] ]

    window = sg.Window('Cayman Islands National Bank™', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Register':
            register_page()
            break
        if event == 'Login':
            print(values)

    window.close()