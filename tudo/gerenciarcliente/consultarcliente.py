import os
from gerenciarcliente.cadastrarcliente import clientes


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class ConsultarCliente:
    def __init__(self):
        self.consultacliente()

    def consultacliente(self):
        limpar_tela()
        codigo = int(input('Insira o codigo do cliente que deseja consultar: '))
        if codigo in clientes:
            print(f'Nome: {clientes[codigo]['nome']}\n cpf: {clientes[codigo]['cpf']}\n endereco: {clientes[codigo]['endereco']}\n telfone: {clientes[codigo]['telefone']}\n email: {clientes[codigo]['email']}')
        else:
         print('Cliente não encontrado')
#transformar em metodos de uma claasse