from flask import Flask, render_template, request, redirect, url_for, flash, session


dados = {}


class Usuario:

  def __init__(self, usuario, senha,cpf):
    self.usuario = usuario
    self.senha = senha
    self.cpf = cpf


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'XUXA'


@app.route('/')
def hello_world():
  return render_template('home.html', log=session)


@app.route('/login')
def teste2():
  return render_template('login.html')


@app.route('/registro')
def principal():
  return render_template('registro.html')


@app.route('/login', methods=['POST'])
def login():
  login = request.form['usuario']
  senha = request.form['senha']

  if not dados.get(login):
    flash('Usuário não existe')
    return render_template('login.html')

  dados_do_usuario = dados.get(login)
  if dados_do_usuario.get('senha') != senha:
    flash('Senha errada')
    return render_template('login.html')

  session['logado'] = login

  return redirect('/')


@app.route('/registro', methods=['POST'])
def cadastro():
  usuario = request.form['usuario']
  senha = request.form['senha']
  confirmsenha = request.form['senha2']

  if dados.get(usuario):
    flash("Usuario já existente")
    return redirect('/registro')

  if senha == confirmsenha:
    dados[usuario] = {'senha': senha}
    print('passei por aqui')
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


@app.route('/v')
def teste():
  texto = ""
  for dado in dados:
    texto += f"usuario: {dado.usuario}, senha: {dado.senha}|| "
  return texto


@app.route('/anuncio')
def anuncio():
  return render_template('anuncio.html')


if __name__ == '__main__':
  app.run(debug=True, )

