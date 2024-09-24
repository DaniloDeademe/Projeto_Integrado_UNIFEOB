import os
from cliente import CadastrarCliente



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class MenuCliente:
    def __init__(self):
        self.exibirmenucliente()

    def exibirmenucliente(self):
        limpar_tela()
        while True:
            print('MENU CLIENTE')
            print('1- Cadastrar Cliente. ')
            print('2- Consultar Cliente. ')
            print('3- Atualizar Cliente. ')
            print('0- Voltar. ')

            opcao = int(input('Escolha uma das opções: '))

            if opcao == 1:
                limpar_tela()
                CadastrarCliente()

            elif opcao == 2:
                limpar_tela()
                ...

            elif opcao == 3:
                limpar_tela()
                ...

            elif opcao == 0:
                limpar_tela()
                print('Voltando ao Menu Principal.')
                break
        
            else:
                limpar_tela()
                print('Error. Tente Novamente.')

