'''
x = int(input("Escreva numero: "))
if x >= 0:
    print("Número introduzido +")
else:
    print("Nº -")
'''

from datetime import date

'''
nome = 'Silvano'
apelido = 'Oliveira'
altura = 1.89
idade = 26
peso = 80
ano = date.today().year
print(nome, apelido, 'com', str(altura)+'m e idade', idade, 'anos, nasceu em', ano - idade)

frase = 'Era uma vez'
print(frase[4:7])
'''

'''nome = 'Joana'
apelido = 'Santos'
idade = 17

frase = f'A {nome} ({apelido}) tem {idade} anos.'
print(frase)'''

'''import math
print(math.pi)'''


'''nome = input('Qual o teu nome?: ')
cor = input('Qual a tua cor favorita?: ')
print(f"O \033[31m'{nome}'\033[0;0m gosta da cor \033[31m'{cor}'\033[0;0m.")'''

'''ano = int(input("Introduza a seu ano de nascimento: "))
print('A sua idade é', (date.today().year - 1) - ano)'''

'''nota = int(input('Qual foi a tua nota da prova? '))
if nota < 50:
    print('Tens défice de sabedoria')
elif nota < 70:
    print('Já foste mais burro')
elif nota < 90:
    print('És quase bom, só falta o quase')
else:
    print('Parabéns, agora toma lá um osso!')'''

'''domingo_faz_sol = True
tenho_boleia = False
if (domingo_faz_sol and not tenho_boleia):
    print('Vou à praia')
else:
    print('Fico em casa')

if (domingo_faz_sol or tenho_boleia):
    print('Vou à praia')
else:
    print('Fico em casa')'''


'''pw = input('Introduza uma password: ')

if len(pw) < 6 or len(pw) > 15:
    print('Palavra passe inválida!')
else:
    print('Palavra passe registada (ñ encriptada)')'''

'''verdade = True
i = 0
j = 100
while verdade:
    if (i < 100):1
        print('#' * i)
        i+=1
    elif (i == 100):
        print('#' * j)
        if (j == 1):
            i = 0
        else:
            j-=1'''

'''import random
num = random.randint(1,6); i = 0
while i < 3:
    i+=1
    x = int(input('Tente adivinhar o numero gerado: '))
    if x == num:
        print('Parabéns! Acertou no numero!')
        break
else:
    print('Falhou, boa sorte para a próxima!')'''


'''import random
num = []; i = 0
while i < 10:
    num.append(random.randint(1,50))
    i+=1
num.sort()
print(num)'''

'''nomes = ['Marcos','Ana','Silvano']
for letras in nomes:
    print('.-=º^º-=-._' * 5)
    print(letras)
for num in range(5):
    print(num)'''

'''numeros = [5,3,7,19,1,3,4,12,6,7]
maior = numeros[0]
for i in numeros:
    if i > maior:
        maior = i
print(maior)
print('Média:', sum(numeros)/len(numeros))'''

'''numeros = [5,3,-7,19,-1,3,4,12,6,7]
menor = numeros[0]
for i in numeros:
    if i < menor:
        menor = i
print(menor)

numeros.sort(reverse=1)
#numeros.reverse()
print(numeros)
print(19 in numeros)'''

'''matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[0][1])

for i in range(3):
    for j in range(3):
        print(matriz[i][j])'''


'''num = [1,3,9,1,5,4,3,9,7,1]
num_unique = []
for i in num:
    if i not in num_unique:
        num_unique.append(i)
print(num_unique)
print(len(num))
'''

'''tupla = (1,2,3,4,5,7,6,7,8,9,0)
print(type(tupla))'''


'''aluno = {
    'nome':'Joaquim Alberto',
    'idade':45,
    'inscrito':'Nos Bombeiros'
}
print(aluno['nome'])
print(aluno.get('ano', 'Não Existe esse CAMPO!!!')) # Usar sempre get para evitar exceções'''

'''resultado = ''
string_num = input('🥹 Escreva um numero de quatro digitos: ')
num_extenso = {
    '1':'Um 1️⃣ ',
    '2':'dois 2️⃣ ',
    '3':'tres 3️⃣ ',
    '4':'quatro 4️⃣ ',
    '5':'cinco 5️⃣ ',
    '6':'seis 6️⃣ ',
    '7':'sete 7️⃣ ',
    '8':'oito 8️⃣ ',
    '9':'nove 9️⃣ ',
    '0':'zero 0️⃣ '
}
for i in string_num:
        resultado += num_extenso.get(i, '!') + ' '
print(resultado)'''


'''def ePar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

x = int(input('Escreva um número: '))
print('O numero é', ePar(x))'''

'''def maior(x, y):
    if x > y:
        return x
    else:
        return y

n = int(input('Escreve um número: '))
n2 = int(input('Escreve outro número: '))
print('O maior número inserido foi', maior(n, n2))'''


# TRY CATCH
'''try:
    idade = int(input('idade: '))
except ValueError:
    print('erro')'''

'''try:
    preco = int(input('Introduza um preço: '))
except ValueError:
    print('Os preço inserido não é valido')

try:
    desc = int(input('introduza o desconto: '))
except ValueError:
    print('O desconto inserido não é valido')

try:
    preco -= preco * (desc/100)
    print(f'preco com desconto {preco}€')
except NameError:
    print('Imposivel calcular desconto!')'''


'''from converter import euro_dolar, dolar_euro, celsius_to_fahrenheit, fahrenheit_to_celsius
print(f'\n{euro_dolar(1)}$')
print(f'{dolar_euro(1)}€')
print(f'{celsius_to_fahrenheit(25)}ºF')
print(f'{fahrenheit_to_celsius(60):.2f}ºC\n')
'''

'''from jogo import Avatar
p1 = Avatar('Joana', 60)
p2 = Avatar('Rita', 80)
p1.mostra_status()
p1.mover_esquerda()
p1.mover_direita()
p1.mover_esquerda()
p1.mostra_status()
p1.alimenta()
p1.mostra_status()'''

'''file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file = open('abc.txt', 'a+')
file.write('Linha Append')
file = open('abc.txt', 'r+')
print('A ler ficheiro: ')
#file.seek(0, 0)
print(file.read())
file.close()
import os
os.remove('abc.txt')'''


import json

d1 = {
    'Pessoa 1': {
        'nome': 'Lara',
        'idade': 25
    },
    'Pessoa 2': {
        'nome': 'Rosa',
        'idade': 25
    },
}
d1_json = json.dumps( d1, indent=True)
print(d1_json)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
    


with open('abc.json','r') as file:
    lerjson = file.read()
    lerjson = json.loads(lerjson)

for k, v in lerjson.items():
    print(k,v)
    for k1, v1 in v.items():
        print(k1,v1)


    










