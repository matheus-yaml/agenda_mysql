from inserir_contato import inserir


while True:
    try:
        while True:
            print('''

            ---------AGENDA-------------

            ADCIONAR CONTATOS       [ 1 ]
            ATUALIZAR CONTATOS      [ 2 ]
            REMOVER CONTATOS        [ 3 ]
            VER CONTATOS            [ 4 ]
            SAIR DA AGENDA          [ 5 ]

            -----------------------------    
            ''')
            opcao = 0 #int(input('Escolha uma das opcoes acima: '))
            if opcao > 5 or opcao < 1:
                opcao =int(input('Escolha apenas uma das OPCOES ACIMA: '))
            break

    except:
        print('Ops... APENAS NÚMEROS, tente novamente! ')

    if opcao == 1:
        inserir()
    elif opcao == 2:
        atualizar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        exibir()
    else:
        break




