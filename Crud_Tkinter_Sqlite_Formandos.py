#Importar os módulos necessários
import tkinter as tk
import sqlite3

#Criar a janela principal e os widgets:
janela = tk.Tk()

# Criar as entradas para os campos nome, idade e e-mail
nome_entry = tk.Entry(janela)
idade_entry = tk.Entry(janela)
email_entry = tk.Entry(janela)
lista = tk.Listbox(janela)
id_entry = tk.Entry(janela)

# Criar os rótulos para cada entrada
nome_label = tk.Label(janela, text="Nome")
idade_label = tk.Label(janela, text="Idade")
email_label = tk.Label(janela, text="E-mail")
id_label = tk.Label(janela, text="Id")
estado_label = tk.Label(janela)

# Criar os botões para adicionar, atualizar e excluir registos
adicionar_btn = tk.Button(janela, text="Adicionar")
atualizar_btn = tk.Button(janela, text="Atualizar")
excluir_btn = tk.Button(janela, text="Excluir")

# Conectar com a base de dados e criar a tabela de pessoas
# Conectar a base de dados
conn = sqlite3.connect('pessoas.db')

# Criar a tabela pessoas
#conn.execute('CREATE TABLE if not exists pessoas (nome TEXT, idade INT, email TEXT)')

#Criar as funções para adicionar, atualizar e excluir registos
def adicionar_registo():
    nome = nome_entry.get()
    idade = idade_entry.get()
    email = email_entry.get()
    # Inserir dados na tabela de pessoas
    conn.execute(f"INSERT INTO pessoas (nome, idade, email) VALUES ('{nome}',{idade},'{email}')")
    conn.commit()
    exibir_registos()
    estado_label.config(text='INSERIDO', fg='green')


def atualizar_registo():
    id = id_entry.get()
    nome = nome_entry.get()
    idade = idade_entry.get()
    email = email_entry.get()
    # Atualizar dados na tabela de pessoas
    conn.execute(f"UPDATE pessoas SET nome = '{nome}', idade = {idade}, email = '{email}' WHERE rowid = {id}")
    conn.commit()
    exibir_registos()
    estado_label.config(text='ATUALIZADO', fg='blue')


def excluir_registo():
    id = id_entry.get()
    # Excluir dados da tabela de pessoas
    conn.execute(f"DELETE FROM pessoas WHERE rowid = {id}")
    conn.commit()
    exibir_registos()
    estado_label.config(text='ELIMINADO', fg='red')


def exibir_registos():
    # Limpar a lista antes de adicionar novos registos
    lista.delete(0, tk.END)
    # Buscar todos os registos na tabela de pessoas
    cursor = conn.execute('SELECT rowid, * FROM pessoas')
    resultados = cursor.fetchall()
    # Adicionar as informações de cada registo à lista
    for resultado in resultados:
        id = resultado[0]
        nome = resultado[1]
        idade = resultado[2]
        email = resultado[3]
        lista.insert(tk.END, f'{id}: {nome}, {idade}, {email}')


# Adicionar os widgets à janela principal

# Adicionar os rótulos e entradas à janela
nome_label.pack()
nome_entry.pack()
idade_label.pack()
idade_entry.pack()
email_label.pack()
email_entry.pack()
lista.pack()
estado_label.pack()
id_label.pack()
id_entry.pack()

# Adicionar os botões à janela
adicionar_btn.pack()
atualizar_btn.pack()
excluir_btn.pack()


#Associar as funções aos botões correspondentes
adicionar_btn.config(command=adicionar_registo)
atualizar_btn.config(command=atualizar_registo)
excluir_btn.config(command=excluir_registo)
exibir_btn = tk.Button(janela, text="Exibir registos", command=exibir_registos)
exibir_btn.pack()

#Iniciar o loop principal do Tkinter
janela.mainloop()