import os

clientes = {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

class CadastrarCliente:
    def __init__(self):
        self.cadastrocliente()

    def cadastrocliente(self):
        limpar_tela()
        codigo = int(input('Insira o codigo deste cliente: '))
        nome = input('Insira o nome do cliente: ')
        cpf = int(input('Insira o cpf do cliente: '))
        endereco = input('Insira o endereço do cliente: ')
        telefone = int(input('Insira o telefone do cliente: '))
        email = input('Insira o email do cliente: ')
        clientes[codigo] = {'nome': nome, 'cpf': cpf, 'endereco': endereco, 'telefone': telefone, 'email': email}
