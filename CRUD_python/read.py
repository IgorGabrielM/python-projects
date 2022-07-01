import os
import sqlite3

def rodaRead():
    nomeBD = input('Nome do banco de dados: ')
    try:
        conector = sqlite3.connect(nomeBD)
        cursor = conector.cursor()
        numRegistros = 0
        cursor.execute('SELECT * FROM AGENDA')
        result = cursor.fetchall()
        for contato in result:
            print('id: %d \nNome: %s \nFone: %s' % (contato))
            numRegistros += 1
        print(numRegistros, 'registros(s)')
        cursor.close()
        conector.close()
    except sqlite3.Error as error:
        print('Erro: BD não encontrado')
        print('Erro: ', error)
        os.remove(nomeBD)