import requests as req

link = 'https://testapi.silvanosfo.repl.co/vendas'

requisicao = req.get(link)
requisicao = requisicao.json()

print(f'Total Vendas: {requisicao["tabela_vendas"]:.2f}')