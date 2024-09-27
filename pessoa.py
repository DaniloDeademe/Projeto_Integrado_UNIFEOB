# Cria a classe pessoa, a qual é usada nas classes de cliente e funcionário
class Pessoa:
    def __init__(self,nome,cpf,endereco,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
# colocar os métodos de cadastro, consulta e alteração em pessoa????