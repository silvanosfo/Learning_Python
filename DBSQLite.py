import sqlite3 as sql
import pandas as pd

bd = sql.connect('basedados.db')

cursor = bd.cursor()

#cursor.execute(f"CREATE TABLE IF NOT EXISTS pessoas (nome text, idade integer, email text)")

#cursor.execute("INSERT INTO pessoas (nome, idade, email) VALUES ('José', 45, 'jose@gmail.com')")

bd.commit()

def exportar_excel():
    cursor.execute("SELECT * FROM pessoas")
    pessoas_registadas = cursor.fetchall()
    pessoas_registadas = pd.DataFrame(pessoas_registadas, columns=['Nome', 'Idade', 'Email'])
    pessoas_registadas.to_excel('pessoas.xlsx')


print('\n')
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
print('\n')

exportar_excel()

excel = pd.read_excel('pessoas.xlsx')
print(excel)

print('\n')
cursor.close()



