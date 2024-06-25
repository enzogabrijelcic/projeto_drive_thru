import re
class Produto:
    def __init__(self,id,nome,valor):
        self.id = id
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
            produto = line.strip().split('Produto: ')[1]
            id = produto.split(':')[1].split(',')[0]
            nome = produto.split(',')[1]
            valor = produto.split(',')[2]
            produto = Produto(id, nome, valor)
            list_p.append(produto)
    return list_p

