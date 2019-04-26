from flask import Flask, request, render_template, redirect, url_for
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
    contatos = get_contatos(cursor)
    cursor.close()
    conn.close()
    return render_template('contatos.html', contatos=contatos)

@app.route('/inserir')
def inserir_contato():
    return render_template('form_cont.html')


@app.route('/inserir_cont', methods=['POST'])
def comfirm_inserir():
    if request.method == 'POST':
        nome = request.form.get('nome')
        tele = request.form.get('tel')
        email = request.form.get('email')
    conn = banco.connect()
    cursor = conn.cursor()
    teste = set_contato(cursor, conn, nome, tele, email)
    if teste:
        cursor.close()
        conn.close()
        return render_template('form_cont.html', erro=teste)
    cursor.close()
    conn.close()
    return redirect(url_for('contatos'))

@app.route('/delete/<idcontato>')
def delete_cont(idcontato):
    conn = banco.connect()
    cursor = conn.cursor()
    delete(cursor, conn, idcontato)
    cursor.close()
    conn.close()
    return redirect(url_for('contatos'))


if __name__ == '__main__':
    app.run(debug=True)