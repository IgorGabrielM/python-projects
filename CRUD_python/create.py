import sqlite3

def rodaCreate():
    nomeBD = input('Nome do banco de dados: ')
    conector = sqlite3.connect(nomeBD)
    cursor = conector.cursor()
    cursor.execute('create table agenda (id integer, nome text, fone text)')
    id = 1
    nome = 'Pessoa'
    while nome != '0':
        print('ID: ', id)
        nome = input('Nome: ')
        if nome != '0':
            fone = input('fone: ')
            cursor.execute('insert into agenda (id, nome, fone) values(?, ?, ?)', (id, nome, fone))
            conector.commit()
            id = id + 1
        else:
            print('Encerrado')
    cursor.close()
    conector.close()
    print('Banco de dados foi criado: ', nomeBD)