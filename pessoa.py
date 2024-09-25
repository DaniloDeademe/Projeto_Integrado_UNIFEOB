# Cria a classe pessoa, a qual é usada nas classes de cliente e funcionário
class Pessoa:
    def __init__(self,nome,cpf,endereco,telefone,email,codigo):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.codigo = codigo

# colocar os métodos de cadastro, consulta e alteração em pessoa????