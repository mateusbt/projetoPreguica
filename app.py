from flask import Flask, render_template, request, redirect, url_for, flash, session
from utilidades import validador

dados = {}
dadosc=[]

class Carro:
  def __init__(self,cidade,modelo,cor,ano,km,descricao,cambio,cambio1,cambio2,imagem,contato,Combustivel,valor):
    self.modelo=modelo
    self.cor=cor
    self.ano=ano
    self.km=km
    self.descricao=descricao
    self.cambio=cambio
    self.cambio1=cambio1
    self.cambio2=cambio2
    self.imagem=imagem
    self.contato=contato
    self.Combustivel=Combustivel
    self.valor=valor
    self.cidade=cidade
    

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

@app.route('/anunciei',methods=['POST'])
def cadastrou():
    if request.method==['POST']:
      modelo= request.form['modelo']
      cor= request.form['cor']
      cidade=request.form['cidade']
      ano= request.form['ano']
      kilometragem=request.form['km']
      contato=request.form['contato']
      descricao=request.form['descricao']
      cambio=request.form['cambio']
      cambio1=request.form['cambio1']
      cambio2=request.form['cambio2']
      imagem=request.form['picture_input']
      Combustivel=request.form['Combustivel']
      valor=request.form['Valor']
      carro=Carro(modelo,cor,cidade,ano,kilometragem,contato,descricao,cambio,cambio1,cambio2,imagem,Combustivel,valor)
      dadosc.append(carro)
      return redirect ('/',dadosc=dadosc)
    else:
      return redirect('/anuncio')

    
@app.route('/perfil')
def perfil_usr():
  return render_template('perfil.html')

@app.route('/carrousr')
def carros_usr():
  return render_template('carrosanunc.html')

@app.route('/modelo',methods=['GET'])
def modelo():
  return render_template('modelo.html',dadosc=dadosc)



if __name__ == '__main__':
  app.run(debug=True, )

