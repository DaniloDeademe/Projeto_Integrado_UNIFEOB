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
            
            match opcao:
                case "1":
                    limpar_tela()
                    CadastrarCliente()
                case "2":
                    limpar_tela()
                    ConsultarCliente()
                case "3":
                    limpar_tela()
                    AtualizarCliente()
                case "0":
                    limpar_tela()
                    print("Voltando...")
                case _: #underline é usado como coringa para capturar qualquer outro caractere.
                    limpar_tela()
                    print('Erro. Selecione uma opção válida.')
            
            # if opcao == 1:
            #     limpar_tela()
            #     CadastrarCliente()

            # elif opcao == 2:
            #     limpar_tela()
            #     ConsultarCliente()

<<<<<<< HEAD
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
=======
            # elif opcao == 3:
            #     limpar_tela()
            #     AtualizarCliente()

            # elif opcao == 0:
            #     limpar_tela()
            #     print('Voltando ao Menu Principal.')
            #     break
>>>>>>> Danilo
        
            # else:
            #     limpar_tela()
            #     print('Error. Tente Novamente.')

