from limpartela import limpartela
from cliente import Cliente

class Menus:
    def __init__(self):
        self.cliente_manager = Cliente()
       
    def menuprincipal(self):
        limpartela()
        while True:
            print('     FERNANDA\n     C̅A̅L̅D̅E̅R̅I̅N̅I̅\n')
            print('1- Gerenciar Produto.')
            print('2- Gerenciar Cliente.')
            print('0- Sair.')

            opcao = input('Escolha uma opção: ')
            
            match opcao:
                case "1":
                    limpartela()
                    self.menuproduto()
                case "2":
                    limpartela()
                    self.menucliente()
                case "0":
                    limpartela()
                    print("Saindo...")
                    break
                case _: #underline é usado como coringa para capturar qualquer outro caractere.
                    print('Erro. Selecione uma opção válida.')


    def menuproduto(self):
        limpartela()
        while True:
            print('GERECIONAMENTO DE PRODUTOS')
            print('1- Cadastrar Produto. ')
            print('2- Consultar Estoque. ')
            print('3- Atualizar Produto. ')
            print('0- Voltar. ')

            opcao = input('Escolha uma opção: ')

            match opcao:
                case "1":
                    limpartela()
                    ...
                case "2":
                    limpartela()
                    ...
                case "3":
                    limpartela()
                    ...
                case "0":
                    limpartela()
                    break
                case _:
                    print('Erro. Selecione uma opção válida.')


    def menucliente(self):
        limpartela()
        while True:
            print('MENU CLIENTE')
            print('1- Cadastrar Cliente. ')
            print('2- Consultar Cliente. ')
            print('3- Atualizar Cliente. ')
            print('0- Voltar. ')

            opcao = input('Escolha uma das opções: ')
            
            match opcao:
                case "1":
                    limpartela()
                    self.cliente_manager.cadastrar()
                case "2":
                    limpartela()
                    self.cliente_manager.consultar()
                case "3":
                    limpartela()
                    ...
                case "0":
                    limpartela()
                    break
                case _: #underline é usado como coringa para capturar qualquer outro caractere.
                    print('Erro. Selecione uma opção válida.')


if __name__ == "__main__":
    menu = Menus()
    menu.menuprincipal()