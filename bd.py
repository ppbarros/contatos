def get_contatos(cursor):
    cursor.execute(f'select nome, telefone, email, idcontatos from contatos')
    contatos = cursor.fetchall()
    return contatos


def set_contato(cursor, conn, nome, tel, email):
    cursor.execute(f'select idcontatos from contatos where nome = "{nome}" and telefone = "{tel}" and email = "{email}"')
    sera = cursor.fetchone()
    if sera is None:
        cursor.execute(f'insert into contatos (nome, telefone, email) values ("{nome}", "{tel}", "{email}")')
        conn.commit()
    else:
        return 'Contato já existente!'


def delete(cursor, conn, idcontato):
    cursor.execute(f'delete from contatos where idcontatos = {idcontato}')
    conn.commit()