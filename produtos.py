import re
class Produto:
    def __init__(self,tipo, id,nome,valor):
        self.id = id
        self.tipo = tipo
        self.nome = nome
        self.valor = valor
    def __repr__(self):
       return f'id: {self.id}, Nome: {self.nome}, Valor: {self.valor}\n'

@staticmethod
def lista_produtos():
    list_p = []
    with open('cardapio_dados.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Produto: '):
            base = line.strip().split('Produto: ')[1]
            tipo = base.split(':')[0]
            id = base.split(':')[1].split(',')[0]
            nome = base.split(',')[1]
            valor = base.split(',')[2]
            produto = Produto(tipo, id, nome, valor)
            list_p.append(produto)
    return list_p