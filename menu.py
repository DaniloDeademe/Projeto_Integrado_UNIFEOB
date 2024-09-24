class Menu:
    def menuprincipal(self):
        while True:
            print('1- Gerenciar Produto.')
            print('2- Gerenciar Cliente.')
            print('0- Sair.')

            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                ...
            elif opcao == 2:
                menucliente()
            elif opcao == 0:
                print('Saindo...')
                break
            else:
                print('Error. Tente Novamente.')
    

    def menucliente(self):
        while True:
            print('1- Cadastrar Cliente.')
            print('2- Consultar Cliente.')
            print('3- Atualizar Cliente.')
            print('0- Voltar.')

            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                ...
            elif opcao == 2:
                ...
            
            elif opcao == 3:
                ...

            elif opcao == 0:
                print('Saindo...')
                break
            else:
                print('Error. Tente Novamente.')
