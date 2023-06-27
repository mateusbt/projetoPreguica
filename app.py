from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world(): 
    return render_template('home.html')

@app.route('/login')
def teste2(): 
    return render_template('login.html')


@app.route('/registro')
def principal():
    return render_template('registro.html')

@app.route('/login',methods=['POST'])
def login():
    login = request.form['usuario']
    senha = request.form['senha']
    if login == 'aluno' and senha == '1234':
        return redirect(url_for('hello_world'))
    else:        
        return redirect(url_for('teste2'))


if __name__ == '__main__':
    app.run(debug=True)