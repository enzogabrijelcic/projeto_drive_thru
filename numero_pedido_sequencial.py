import os

def ler_ultimo_pedido():
    if os.path.exists("ultimo_pedido.txt"):
        with open("ultimo_pedido.txt", "r") as file:
            return int(file.read().strip())
    return 0

def salvar_ultimo_pedido(numero):
    with open("ultimo_pedido.txt", "w") as file:
        file.write(str(numero))

def gerar_numero_pedido():
    ultimo_pedido = ler_ultimo_pedido()
    novo_pedido = ultimo_pedido + 1
    salvar_ultimo_pedido(novo_pedido)
    return novo_pedido

# Gerar um novo número de pedido