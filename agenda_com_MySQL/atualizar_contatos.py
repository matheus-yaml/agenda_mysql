import mysql.connector
from inserir_contato import Telefone, Celular
from exibir_contatos import ver_todos


uuser = 'epiz_22941340'
ppassowrd = 'xxx'
hhost = 'sql100.epizy.com'
ddatabase = 'epiz_22941340_meu_banco'


def atualizar():
    global telefone, celular
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()


    while True:
        while True:
            ver_todos()
            try:
                id = ''
                if len(str(id)) < 1:
                    id = int(input('Digite um ID PARA EDITAR o contato: '))

            except:
                print('Ops... Este campo não pode ficar vazio \n')
            if len(str(id)) > 0:
                break



#        if len(str(id)) > 1:
        id = str(id)
        id = f'{id}'

        print(f'Contato {id} selecionado. Insira os dados atalizados do contato')

        while True:
            nome = str(input('Nome do contato: '))
            if len(nome) > 30:
                print('Tente novamente, use no maximo 30 caracteres: ')
                nome = str(input('Nome do contato: '))
            elif len(nome) == 0:
                print('Tente novamente, esse campo não pode ficar vazio: ')
                nome = str(input('Nome do contato: '))
            elif nome in '1 2 3 4 5 6 7 8 9 0':
                print('Tente novamente, esse campo não pode conter números: ')
                nome = str(input('Nome do contato: '))
            break
        telefone = Telefone()
        celular = Celular()

        telefone = str(telefone)
        celular = str(celular)
        telefone = f'({telefone[0:2]}){telefone[2:6]}-{telefone[6:10]}'
        celular = f'({celular[0:2]}){celular[2:7]}-{celular[7:11]}'

        cursor.execute(f'update agenda.contatos set nome = "{nome}", telefone = "{telefone}", celular = "{celular}" where id = "{id}"')
        conexao.commit()
        cursor.close()
        conexao.close()
        break
