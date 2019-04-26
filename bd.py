def get_contatos(cursor):
    cursor.execute(f'select nome, telefone, email from contatos')
    contatos = cursor.fetchall()
    return contatos
