import PySimpleGUI as sg
import webbrowser as wb
import mysql.connector

mydb = mysql.connector.connect(
    host = '**.**.**.***',
    user = 'geral',
    password = 'teclaDo+4',
    database = 'dbpysimplegui_sil'
)

sg.theme('DarkBlue7')

layout = [
    [sg.Text('Utilizador')],
    [sg.Input(key='utilizador')],
    [sg.Text('Password')],
    [sg.Input(key='password')],
    [sg.Button('Entrar')],
    [sg.Text('', key='mensagem')],
    [sg.Button('Inserir novo login')]
]

window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif event == 'Entrar':
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM logins WHERE utilizador = '{values['utilizador']}' AND password = '{values['password']}'")
        result = cursor.fetchone()
        if result:
            window['mensagem'].update('Login efetuado com sucesso!')
            url = 'https://rezmason.github.io/matrix/'
            wb.open_new_tab(url)
            window.close()
        else:
            window['mensagem'].update('Credencial erradas!')
    elif event == 'Inserir novo login':
        novo_utilizador = sg.popup_get_text('Digite o novo nome do utilizador: ')
        nova_password = sg.popup_get_text(f'Digite uma password para o utilizador {novo_utilizador}')
        cursor = mydb.cursor()
        cursor.execute(f"INSERT INTO logins (utilizador, password) VALUES ('{novo_utilizador}','{nova_password}')")
        mydb.commit()
        sg.popup('Conta criada com sucesso!')
        window.close()


window.close()