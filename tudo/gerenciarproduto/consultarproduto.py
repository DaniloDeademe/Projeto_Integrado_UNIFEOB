import os
from gerenciarproduto.cadastrarproduto import produtos


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class ConsultarProduto:
    def __init__(self):
        self.consultaproduto()


    def consultaproduto(self):
        limpar_tela()
        codigo = int(input('Insira o codigo do produto que deseja consultar: '))
        if codigo in produtos: 
            print(f'Nome: {produtos[codigo]['nome']}\n Descrição: {produtos[codigo]['descricao']}\n Cor: {produtos[codigo]['cor']}\n  Tamanho: {produtos[codigo]['tamanho']}\n Preço R$: {produtos[codigo]['preco']}\n Quantidade em Estoque: {produtos[codigo]['quantidade']}')
        else:
            limpar_tela()
            print('Produto não encontrado.')

#transformar em metodos de uma claasse