import mysql.connector

def exibir():

    conexao = mysql.connector.connect(user ='root', password = 'db', host = 'localhost', database = 'agenda')

    cursor = conexao.cursor()

    exibir = cursor.execute('select * from agenda.contatos)

    for linha in exibirr:
        print(linha)