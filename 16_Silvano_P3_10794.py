import tkinter as tk
import sqlite3

janela = tk.Tk()
janela.title("Agenda")

nome_label = tk.Label(janela, text="Nome")
nome_entry = tk.Entry(janela)

sexo_label = tk.Label(janela, text="Sexo")
sexo_entry = tk.Entry(janela)

telefone_label = tk.Label(janela, text="Telefone")
telefone_entry = tk.Entry(janela)

email_label = tk.Label(janela, text="Email")
email_entry = tk.Entry(janela)

id_label = tk.Label(janela, text="Id")
id_entry = tk.Entry(janela)

conn = sqlite3.connect('silvano.db')

#Criar a tabela pessoas
#conn.execute('CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, sexo TEXT, telefone INT, email TEXT)')

c = conn.cursor()

#c.execute()

def inserir_dados():    
    nome = nome_entry.get()
    sexo = sexo_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    # Inserir dados na tabela de pessoas
    conn.execute(f"INSERT INTO pessoas (nome, sexo, telefone, email) VALUES ('{nome}', '{sexo}', {telefone}, '{email}')")
    conn.commit()
    exibir_dados()


def exibir_dados():
    # Limpa as caixas de texto
    limpar_campos()
    # Limpar a Text antes de adicionar novos registos
    texto.delete(1.0, tk.END)
    # Buscar todos os registos na tabela de pessoas
    c.execute('SELECT rowid, * FROM pessoas')
    resultados = c.fetchall()
    # Adicionar as informações de cada registo à Text
    for resultado in resultados:
        id = resultado[0]
        nome = resultado[1]
        sexo = resultado[2]
        telefone = resultado[3]
        email = resultado[4]
        texto.insert(tk.END, f'{id}: {nome}, {sexo}, {telefone}, {email}\n')


def atualizar_dados():    
    id = id_entry.get()
    nome = nome_entry.get()
    sexo = sexo_entry.get()
    telefone = telefone_entry.get()
    email = email_entry.get()
    # Atualizar dados na tabela de pessoas
    conn.execute(f"UPDATE pessoas SET nome = '{nome}', sexo = '{sexo}', telefone = {telefone}, email = '{email}' WHERE rowid = {id}")
    conn.commit()
    exibir_dados()


def apagar_dados():
    id = id_entry.get()
    # Excluir dados da tabela de pessoas
    conn.execute(f"DELETE FROM pessoas WHERE rowid = {id}")
    conn.commit()
    exibir_dados()


def limpar_campos():
    id_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    sexo_entry.delete(0, tk.END)
    telefone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


inserir_button = tk.Button(janela, text="Inserir", command=inserir_dados)

exibir_button = tk.Button(janela, text="Exibir", command=exibir_dados)

atualizar_button = tk.Button(janela, text="Atualizar", command=atualizar_dados)

apagar_button = tk.Button(janela, text="Apagar", command=apagar_dados)

texto = tk.Text(janela, height=20, width=60)

nome_label.grid(row=0, column=0)
nome_entry.grid(row=0, column=1)

sexo_label.grid(row=1, column=0)
sexo_entry.grid(row=1, column=1)

telefone_label.grid(row=2, column=0)
telefone_entry.grid(row=2, column=1)

email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)

id_label.grid(row=0, column=4)
id_entry.grid(row=1, column=4)

inserir_button.grid(row=2, column=3)
atualizar_button.grid(row=2, column=4)
apagar_button.grid(row=3, column=4)
exibir_button.grid(row=3, column=3)

texto.grid(row=5, columnspan=6, padx=20, pady=20)

janela.mainloop()

conn.close()
