class Cadastro:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
    def __repr__(self):
        return f'{self.nome}\n {self.cpf}\n, {self.senha}'
    
       