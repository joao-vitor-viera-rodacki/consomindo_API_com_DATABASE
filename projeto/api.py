from flask import Flask , request
import sqlite3 as sq

import data

banco = sq.connect('database.db')
cursor = banco.cursor()

app = Flask('Clientes')

@app.route('/cadastra_usu', methods=['POST'])
def cadastra_usu():
  
    body = request.get_json()

    print(body)
    if ('nome' not in body):
        return geraResponse(400, "O nome é obrigatorio!")
    
    if ('idade' not in body):
        return geraResponse(400, "A idade é obrigatoria")
    
    if ('email' not in body):
        return geraResponse(400, "O email é obrigatorio")
    
    usuario_dados = data.cadastra_usu(body["nome"], body["idade"], body["email"])
    print(usuario_dados)
    return geraResponse(200, 'User Criado!', 'User', usuario_dados)



@app.route('/excluir_usu',methods=['POST'])
def excluir_usu():
    body = request.get_json()

    if ('nome' not in body):
        return geraResponse(400, "O nome é obrigatorio!")
 

    usuario_dados = data.excluir_usu('nome', body['nome'])
    return geraResponse(200,'Usuario deletado com sucesso!!','user', usuario_dados)


@app.route('/alterar_nome', methods=['POST'])
def alterar_nome():
    body = request.get_json()

    if ('nome' not in body):
        return geraResponse(400, "O nome é obrigatorio!")
    if ('alteracao' not in body):
        return geraResponse(400, "A alteração que vai ser feita é obrigatoria")
  

    usuario_dados = data.alterar_nome(nome=body['nome'], alteracao=body['alteracao'])
    
    return geraResponse(200, 'usuario modificado', 'user', usuario_dados)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):    
    response = {}
    response['status'] = status
    response['mesagem'] = mensagem

    if (nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response


app.run()
