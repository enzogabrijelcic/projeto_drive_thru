class Usuario:
    def __init__(self, nome, cpf:int, senha:int):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
    def __repr__(self):
        return f'{self.nome}\n {self.cpf}\n, {self.senha}'
    
    def from_string(user_str):
        nome, cpf, senha = user_str.split(',')
        return Usuario(nome, cpf, senha)
       