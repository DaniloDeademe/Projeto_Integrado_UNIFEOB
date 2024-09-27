#criar a classe funcionário para ser usado na venda como o funcionário que realizou a venda
import random
from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome,cpf,endereco,telefone,email,codigo,cargo,salario,data_admissao):
        super().__init__(nome,cpf,endereco,telefone,email, codigo)
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao
        
    def cadastrarFuncionario(self):
        nome = input("Digite o nome completo do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        salario = input("Digite o salário do funcionário: ")
        data_admissao = input("Digite a data de admissão do funcioário: ")
        codigo = random.randint(1000, 9999)
        
    def atualizarFuncionario(self):
        pass
    
    def consultarFuncionario(self):
        #if codigo in Funcionario
        pass
    print("Alguma coisa")