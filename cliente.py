class Cliente:
    def __init__(self, nome, cpf, endereco, telefone, email, codigo):
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf
        
    
    def cadastrarcliente(self):
        codigo = int(input('Insira o codigo deste cliente: '))
        nome = input('Insira o nome do cliente: ')
        cpf = int(input('Insira o cpf do cliente: '))
        endereco = input('Insira o endereço do cliente: ')
        telefone = int(input('Insira o telefone do cliente: '))
        email = input('Insira o email do cliente: ')
    
    
