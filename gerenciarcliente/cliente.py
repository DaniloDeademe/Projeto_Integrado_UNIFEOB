from pessoa import Pessoa


clientes = {}

class CadastrarCliente(Pessoa):
    def __init__(self, endereco, telefone, email, codigo):
        super().__init__(nome, idade, cpf)
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.codigo = codigo
        
        codigo = int(input('Insira o codigo deste cliente: '))
        nome = input('Insira o nome do cliente: ')
        cpf = int(input('Insira o cpf do cliente: '))
        endereco = input('Insira o endereço do cliente: ')
        telefone = int(input('Insira o telefone do cliente: '))
        email = input('Insira o email do cliente: ')
        clientes[codigo] = {'nome': nome, 'cpf': cpf, 'endereco': endereco, 'telefone': telefone, 'email': email}
#transformar em metodos de uma classe