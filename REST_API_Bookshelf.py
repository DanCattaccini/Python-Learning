#Exemplo de app de gerenciamento de uma lista de livros
#API é um lugar para disponibilizar recursos e;ou funcionalidades
# 1 - Objetivo
# 2 - URL Base
# 3 - Endpoints (recursos/funcionalidades)
# 4 Quais recursos

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
          'titulo': 'O senhor dos aneis - a sociedade do anel',
          'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 2,
          'titulo': 'Harry Potter e a Pedra Filosofal',
          'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
          'titulo': 'James Clear',
          'autor': 'Hábitos Atômicos'
    },
]

#Consult(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consult(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro) 

#Edit
@app.route('/livros/<int:id>, methods=[PUT]')
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Create
@app.route('/livros/<int:id>, methods=[POST]')
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Exclude
@app.route('/livros/<int:id>, methods=[DELETE]')
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)

