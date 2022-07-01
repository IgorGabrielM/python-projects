import sqlite3, os

nomeBD = input('Digite o nome do banco de dados: ')
try:
    conector = sqlite3.connect(nomeBD)
    id = '1'
    cursor = conector.cursor()
    while id != '0':
        id = input('Digite o indice [0 - Sair]: ')
        if id != '0':
            cursor.execute('select * from agenda where id=?', (id))
            result = cursor.fetchall()
            achei = False
            for contato in result:
                print('id: %d \nNome: %s \nFone: %s' % (contato))
            if not achei:
                print('Erro: Contato não encontrado')
    cursor.close()
    conector.close()
except sqlite3.Error as error:
    print('Erro: BD não encontrado')
    print('Erro: ', error)
    os.remove(nomeBD)