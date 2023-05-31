import requests as req
import tkinter as tk

root = tk.Tk()
root.geometry('600x500')
root.title('API')

#https://minhaapi.marcosalvaraes.repl.co/totalvendas

Link_label = tk.Label(root, text="ENDEREÇO DA API", height = 2, width = 50)
Link_label.pack()
Link_entry = tk.Entry(root, width=50)
Link_entry.pack()

def ler_api():
    requisicao =  req.get(Link_entry.get())
    requisicao = requisicao.json()
    #Formata texto em variável
    vendas = f"Total de vendas de TV:      {requisicao['total_vendas_Tv']:.2f}\n"
    vendas += f"Total de vendas de rádio:  {requisicao['total_vendas_Radio']:.2f}\n"
    vendas += f"Total de vendas de jornal: {requisicao['total_vendas_Jornal']:.2f}\n"
    vendas += f"Total de vendas:           {requisicao['total_vendas_Vendas']:.2f}\n"
    #Insere no widget Text
    caixa_texto.insert(tk.END, vendas)
    #Limpa widget Entry
    Link_entry.delete(0, tk.END)
    #Cria e guarda (ou substitui) conteudo em ficheiro
    with open('16_SilvanoAPI.txt', 'w+') as ficheiro:
        ficheiro.write(vendas)


def ler_temperatura():
    # API key openweathermap
    API_KEY =  '02ce3117223858290ecc99b227f0577d'
    # Coordinates Barcelos
    LAT = '41.5387600'
    LON = '-8.6150500'
    LANG = 'pt'
    link = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&lang={LANG}&appid={API_KEY}&units=metric"
    temperaturas = req.get(link)
    temperaturas = temperaturas.json()
    local = temperaturas["name"]
    desc = temperaturas["weather"][0]["description"]
    temp = temperaturas["main"]["temp"]
    caixa_texto.insert(tk.END, f'Local: {local} | Tempo: {desc} | Temperatura: {temp}ºC\n')


def ler_cotacao():
    cotacoes = req.get('https://economia.awesomeapi.com.br/json/last/EUR-USD,EUR-BRL,BTC-USD')
    cotacoes = cotacoes.json()
    caixa_texto.insert(tk.END, f'Cotacoes de moedas: EURUSD: {cotacoes["EURUSD"]["bid"]}$ | BTCUSD: {cotacoes["BTCUSD"]["bid"]}$\n')


# Cria o botão para ler o link
Link_label = tk.Label(root, text="", height = 2, width = 50)
Link_label.pack()
api_botao = tk.Button(root, text='LER API', height = 2, width = 50, pady=10, command=ler_api) 
api_botao.pack()
temperatura_botao = tk.Button(root, text='LER TEMPERATURA ATUAL', height = 2, width = 50, pady=10, command=ler_temperatura) 
temperatura_botao.pack()
cotacao_botao = tk.Button(root, text='LER COTAÇÃO MOEDA', height = 2, width = 50, pady=10, command=ler_cotacao) 
cotacao_botao.pack()
Link_label = tk.Label(root, text="", height = 2, width = 50)
Link_label.pack()

# Cria a caixa de texto para exibir os resultados
caixa_texto = tk.Text(root)
caixa_texto.pack()

root.mainloop()