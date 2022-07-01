from create import rodaCreate
from read import rodaRead
from update import rodaUpdate
from delete import rodaDelete
print('Menu dos arquivos: \nDigite 0 para sair do meunu \nDigite 1 para cirar um banco\nDigite 2 para ler um banco \n'
      'Digite 3 para inserir um dado no banco \nDigite 4 para deletar um dado no banco')

i = input('Digite sua entrada: ')
while i != '0':
    if i == '1':
        rodaCreate()
        i = input('Digite sua entrada: ')
    elif i == '2':
        rodaRead()
        i = input('Digite sua entrada: ')
    elif i == '3':
        rodaUpdate()
        i = input('Digite sua entrada: ')
    elif i == '4':
        rodaDelete()
        i = input('Digite sua entrada: ')
    elif i == '0':
        print('Você saiu')
    else:i = input('A entrada que você digitou não é valida, digite uma entrada valida: ')
