#criar a classe funcionário para ser usado na venda como o funcionário que realizou a venda
from pessoa import Pessoa

class Funcionario:
    def __init__(self,nome,cpf,cargo,salario,data_admissao):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        
    def cadastrarFuncionario(self):
        nome = input("Digite o nome completo do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        salario = input("Digite o salário do funcionário: ")
        data_admissao = input("Digite a data de admissão do funcioário: ")
        
    def atualizarFuncionario(self):
        pass