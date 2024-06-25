import time,os
from produtos import *
pagamento = 0 # conta a pagar no final 

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')

def verificar_produto(x):
    aux = False
    for produto_v in lista_produtos():
        if produto_v.id == x:
            aux = True
            break
    if aux:
        pass
    else:
        print("produto não encontrado")

def hamburguers():
    global pagamento
    for produto in lista_produtos():
        if produto.tipo == "hamburguer":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")
    x = input("Selecione o codigo do produto que deseja adicionar ao carrinho\n")
    verificar_produto(x)
    for produto_v in lista_produtos():
        if produto_v.id == x:
            pagamento =+ int(produto.valor) 
            print(produto_v.nome,"adicionado ao carrinho")
            break
        

    return pagamento

def acompanhamentos():
    global pagamento
    for produto in lista_produtos():
        if produto.tipo == "acompanhamento":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")    
    return pagamento

def bebidas():
    for produto in lista_produtos():
        if produto.tipo == "bebida":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")    
    global pagamento 
    pass

def sobremesas():
    global pagamento 
    for produto in lista_produtos():
        if produto.tipo == "sobremesa":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")    
    pass

def combos():
    pass

hamburguers()
print("valor a pagar:",pagamento)