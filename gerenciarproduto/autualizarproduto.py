import os
from gerenciarproduto.cadastrarproduto import produtos


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class AtualizarProduto:
    def __init__(self):
        self.atualizaproduto()


    def atualizaproduto(self):
        limpar_tela()
        codigo = int(input('Insira o codigo do produto que deseja atualizar: '))
    
        if codigo in produtos:
            nome = input('Insira o nome do produto: ')
            descricao = input('Insira a descrição do produto: ')
            cor = input('Insira a cor do produto: ')
            tamanho = float(input('Insira o tamanho do produto: '))
            preco = float(input('Insira o preço do produto: '))
            quantidade = int(input('Insira a quantidade do produto: '))
            produtos[codigo] = {'nome': nome, 'descricao': descricao, 'cor': cor, 'tamanho': tamanho, 'preco': preco, 'quantidade': quantidade}
            limpar_tela()
        else:
            limpar_tela()
            print('Error. Tente Novamente.')