from flask import Flask, render_template, request, redirect, url_for, flash, session
from projetoPreguica.utilidades import validador

dados = {}


class Usuario:

  def __init__(self, usuario, senha,cpf):
    self.usuario = usuario
    self.senha = senha
    self.cpf = cpf


app = Flask(__name__)

app.config['SECRET_KEY'] = 'XUXA'


@app.route('/h')
def hello_world():
  return render_template('home.html', log=session)


@app.route('/login')
def teste2():
  return render_template('login.html')


@app.route('/registro')
def principal():
  return render_template('registro.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
  login = request.form['usuario']
  senha = request.form['senha']
  cpf = (request.form['cpf'])

  print(dados)
  if not validador(cpf):
    flash("cpf invalido")
    return redirect('/login')
  
  if not dados.get(login):
    flash('Usuário não existe')
    return render_template('login.html')

  if not dados.get(login).get('cpf') == cpf:
    flash('cpf invalido')
    return render_template('login.html')
  

  dados_do_usuario = dados.get(login)
  if dados_do_usuario.get('senha') != senha:
    flash('Senha errada')
    return render_template('login.html')

  session['logado'] = login

  return redirect('/h')


@app.route('/registro', methods=['POST'])
def cadastro():
  usuario = request.form['usuario']
  senha = request.form['senha']
  cpf = request.form['cpf']
  confirmsenha = request.form['senha2']

  if not validador(cpf):
    flash("cpf invalido")
    return redirect('/registro')
  
  if dados.get(usuario):
    flash("Usuario já existente")
    return redirect('/registro')

  if senha == confirmsenha:
    dados[usuario] = {'senha': senha ,'cpf' : cpf}
    return redirect("/login")

  else:
    flash("Senhas diferentes")
    return render_template('registro.html')


@app.route('/carro')
def auditt():
  return redirect('/anuncio')


@app.route('/sair')
def sair():
  del session['logado']
  return redirect('/login')


@app.route('/anuncio')
def anuncio():
  return render_template('anuncio.html')

@app.route('/anunciar')
def anuncie():
  return render_template('venda.html')


if __name__ == '__main__':
  app.run(debug=True, )

