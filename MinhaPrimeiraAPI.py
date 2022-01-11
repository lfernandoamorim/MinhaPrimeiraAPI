#Antes de começar:
#1) precisa instalar o pandas e o flask
#2) ter uma base de dados para esse exemplo (BaseExemploAPI)

#importa o pacote Pandas e deixa com o nome pd
import pandas as pd

#importa o flask
from flask import Flask, jsonify

#para inicializar um aplicativo do Flask que será a API
app = Flask(__name__)

#contruindo as funcionalidades
@app.route('/')
def homepage():
  return 'A Minha Primeira API está Online!!!'

@app.route('/piloto')
def piloto():
  return 'Está agora na página Piloto'

@app.route('/pegarvendas')
def pegarvendas():
  #Alimenta a variável tabela com a informação do BaseExemploAPI.csv
  tabela = pd.read_csv('BaseExemploAPI.csv')

  #soma o toral da coluna Vendas
  total_vendas = tabela['Vendas'].sum()

  #a variável resposta como um dicionário para quem vai consumir a API
  resposta = {'total_vendas': total_vendas}

  #Retorna a variável resposta como JSON utilizando
  #o dicionário do Flask chamado jsonify()
  return jsonify(resposta)


#rodar o app, isto é, API. Para rodar no servidor da Replit e ficar open
#informe o host='0.0.0.0'
app.run(host='0.0.0.0')

'''
#Exibe a tabela
print(tabela)

#Exibe o total_vendas
print(total_vendas)
'''