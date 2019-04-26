from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *
app = Flask(__name__)
banco = MySQL()
banco.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'contatos'

@app.route('/')
def principal():
    return render_template('home.html')

@app.route('/listar')
def contatos():
    conn = banco.connect()
    cursor = conn.cursor()
    return render_template('contatos.html', contatos=get_contatos(cursor))

@app.route('/inserir', method = ['POST'])
def inserir_contato()
    return

if __name__ == '__main__':
    app.run()