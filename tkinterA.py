import tkinter as tk
import tkinter.messagebox as tkmsg
import json
import requests as req

root = tk.Tk()
root.title('Aula')
root.minsize(width=480, height=320)

nome_label = tk.Label(root, text='Nome')
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

endereco_label = tk.Label(root, text='Endereço')
endereco_label.pack()
endereco_entry = tk.Entry(root)
endereco_entry.pack()

codpost_label = tk.Label(root, text='Código Postal')
codpost_label.pack()
codpost_entry = tk.Entry(root)
codpost_entry.pack()

telefone_label = tk.Label(root, text='Telefone')
telefone_label.pack()
telefone_entry = tk.Entry(root)
telefone_entry.pack()


# Não funciona no MACOSX
#root.iconbitmap('iconmac.icns')

def salvar_contacto():
    # adquirir os valores das caixas de texto em variaveis
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    codpost = codpost_entry.get()
    telefone = telefone_entry.get()
    # guardar em ficheiro
    with open('contactos.txt', 'a') as ficheiro:
        ficheiro.write(f'Nome: {nome} | Endereço: {endereco} | Código Postal: {codpost} | Telefone: {telefone}\n')
        limpa_caixa()


def ver_contactos():
    with open('contactos.txt', 'r+') as lista:
        # Atualiza a label com o conteudo
        #contactos_label.config(text=lista.read())
        tkmsg.showinfo(title='Lista de Contactos', message=lista.read())
    

contactos_label = tk.Label(root)
contactos_label.pack()

def limpa_caixa():
    nome_entry.delete(0, tk.END)
    endereco_entry.delete(0, tk.END)
    codpost_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)


def limpa_ficheiro():
    with open('contactos.txt', 'w') as file:
        pass


def mostra_cotacoes():
    cotacoes = req.get('https://economia.awesomeapi.com.br/json/last/EUR-USD,EUR-BRL,BTC-USD')
    cotacoes = cotacoes.json()
    tkmsg.showinfo('Cotacoes de moedas', message=f'\nEURUSD: {cotacoes["EURUSD"]["bid"]}$\nBTCUSD: {cotacoes["BTCUSD"]["bid"]}$\n')


# Botão para fazer OK e Executar função salvar_contacto()
salvar_botao = tk.Button(root, text='Guardar', command=salvar_contacto)
salvar_botao.pack()

lista_contactos = tk.Button(root, text='Ver contactos', command=ver_contactos)
lista_contactos.pack()

apaga_ficheiro = tk.Button(root, text='Limpar contactos', command=limpa_ficheiro)
apaga_ficheiro.pack()

buscar_cotacoes = tk.Button(root, text='Buscar Cotacoes', command=mostra_cotacoes)
buscar_cotacoes.pack()

root.mainloop()