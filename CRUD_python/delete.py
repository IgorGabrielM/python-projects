import sqlite3, os

def rodaDelete():
    nomeBD = input('Nome do banco de dados: ')
    try:
        conector = sqlite3.connect(nomeBD)
        id = '1'
        cursor = conector.cursor()
        while id != '0':
            id = input('Digite o indice [0 - Sair]: ')
            if id != '0':
                cursor.execute('delete from agenda where id=?', (id))
                conector.commit()
                print('Okay, contato removido')
        cursor.close()
        conector.close()
    except sqlite3.Error as error:
        print('Erro: BD não encontrado')
        print('Erro: ', error)
        os.remove(nomeBD)