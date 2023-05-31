import PySimpleGUI as sg
import webbrowser as wb

sg.theme('DarkBlue7')

layout = [
    [sg.Text('Utilizador')],
    [sg.Input(key='utilizador')],
    [sg.Text('Password')],
    [sg.Input(key='password')],
    [sg.Button('Entrar')],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif event == 'Entrar':
        password_check = '123.Abc'
        username_check = 'Silvano'
        username = values['utilizador']
        password = values['password']
        if password == password_check and username == username_check:
            window['mensagem'].update('Login efetuado com sucesso!')
            url = 'https://rezmason.github.io/matrix/'
            wb.open_new_tab(url)
        elif username == username_check and password != password_check:
            window['mensagem'].update('Password Inválida!')
        else:
            window['mensagem'].update('Username nao reconhecido!')

window.close()