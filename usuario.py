class Usuario:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def to_string(self):
        return f"{self.nome},{self.cpf},{self.senha}"

    @staticmethod
    def from_string(string):
        nome, cpf, senha = string.strip().split(',')
        return Usuario(nome, cpf, senha)
