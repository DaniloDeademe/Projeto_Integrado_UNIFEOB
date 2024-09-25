import os
from menus.menuproduto import MenuProduto
from menus.menucliente import MenuCliente

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class MenuPrincipal:
    def __init__(self):
        self.exibirmenu()

    def exibirmenu(self):
        limpar_tela()
        while True:
            print('1- Gerenciar Produto.')
            print('2- Gerenciar Cliente.')
            print('0- Sair.')

            opcao = int(input('Escolha uma opção: '))
            
            match opcao:
                case "1":
                    limpar_tela()
                    MenuProduto()
                case "2":
                    limpar_tela()
                    MenuCliente()
                case "3":
                    limpar_tela()
                    RelizarVenda()
                case "0":
                    limpar_tela()
                    print("Saindo...")
                case _: #underline é usado como coringa para capturar qualquer outro caractere.
                    limpar_tela()
                    print('Erro. Selecione uma opção válida.')
            
            # if opcao == 1:
            #     limpar_tela()
            #     MenuProduto()
            # elif opcao == 2:
            #     limpar_tela()
            #     MenuCliente()
            # elif opcao == 0:
            #     limpar_tela()
            #     print('Saindo...')
            #     break
            # else:
            #     limpar_tela()
            #     print('Error. Tente Novamente.')

print()
