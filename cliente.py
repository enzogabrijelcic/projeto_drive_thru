class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
    def __repr__(self):
        return f'{self.nome}, {self.cpf}, {self.senha}'
    
    @staticmethod
    def from_string(user_str):
        nome, senha = user_str.split(',')
        return Cliente(nome, cpf, senha)