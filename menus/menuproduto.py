import os
from gerenciarproduto.cadastrarproduto import CadastrarProduto
from gerenciarproduto.consultarproduto import ConsultarProduto
from gerenciarproduto.autualizarproduto import AtualizarProduto

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class MenuProduto:
    def __init__(self):
        self.exibirmenuproduto()

    def exibirmenuproduto(self):
        limpar_tela()
        while True:
            print('GERECIONAMENTO DE PRODUTOS')
            print('1- Cadastrar Produto. ')
            print('2- Consultar Estoque. ')
            print('3- Atualizar Produto. ')
            print('0- Voltar. ')

            opcao = int(input('Escolha uma opção: '))
    
            if opcao == 1:
                limpar_tela()
                CadastrarProduto()

            elif opcao == 2:
                limpar_tela()
                ConsultarProduto()

            elif opcao == 3:
                limpar_tela()
                AtualizarProduto()

            elif opcao == 0:
                limpar_tela()
                print('Voltando ao menu principal.')
                break
            else:
                limpar_tela() 
                print('Error. Tente Novamente.')
