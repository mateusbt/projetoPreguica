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




if __name__ == '__main__':
    app.run(debug=True)