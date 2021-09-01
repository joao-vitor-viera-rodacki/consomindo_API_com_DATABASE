import sqlite3 as sq



#cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')

'''
def inicia():
    banco = sq.connect('database.db')
    cursor = banco.cursor()
'''
def cadastra_usu (nome, idade, email):
    banco = sq.connect('database.db')
    cursor = banco.cursor()

    cursor.execute(f'INSERT INTO pessoas VALUES("{nome}",{idade},"{email}")')
    banco.commit()
    

def excluir_usu(nome,  caracter=False, idade=False, integer=False):
    banco = sq.connect('database.db')
    cursor = banco.cursor()    
    
    if integer :

        cursor.execute(f'DELETE from pessoas where idade {caracter}= {idade}')
        banco.commit()

    else:
        cursor.execute(f'DELETE from pessoas where nome = "{nome}"')
        banco.commit()

def ler_usu(condicao, caracter, integer=False):
    
    if integer:
        sql = f'SELECT * FROM pessoas WHERE idade {condicao}= {caracter}'
    else:
        sql = f'SELECT * FROM pessoas WHERE {condicao} = "{caracter}"'
    
    for row in cursor.execute(sql):
        print(row)

def alterar_nome( nome, alteracao):
    
    banco = sq.connect('database.db')
    cursor = banco.cursor() 
    
    if nome:
            
        cursor.execute(f'UPDATE pessoas set nome = "{alteracao}" WHERE nome = "{nome}"')
        banco.commit()

    



#test.cadastra_usu('boboo',24,'test@gmail.com')
#excluir_usu('nome', 'e')
#test.ler_usu('>', 23, True)
#test.alterar_dados(email='test@gmail.com')
#banco.commit()
