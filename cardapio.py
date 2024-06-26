import time,os
from formatação import *
from produtos import *
pagamento = 0 # conta a pagar no final 

def atendimento():
    global pagamento
    typing("\nSelecione o codigo do produto que deseja adicionar ao carrinho")
    x = input("\n")
    verificar_produto(x)
    for produto_v in lista_produtos():
        if produto_v.id == x:
            pagamento += int(produto_v.valor) 
            typing(f'{produto_v.nome} adicionado ao carrinho')
            typing(f"Conta atual: R${pagamento}\n")
            time.sleep(2)
            break
    return pagamento 

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
    for produto in lista_produtos():
        if produto.tipo == "hamburguer":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")
    atendimento()

def acompanhamentos():
    for produto in lista_produtos():
        if produto.tipo == "acompanhamento":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")
    atendimento()

def bebidas():
    for produto in lista_produtos():
        if produto.tipo == "bebida":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")   
    atendimento()  

def sobremesas(): 
    for produto in lista_produtos():
        if produto.tipo == "sobremesa":
            print(f"[{produto.id}] {produto.nome} - R${produto.valor}")    
    atendimento()

def combos():
    pass