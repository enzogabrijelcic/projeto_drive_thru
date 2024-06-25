import time
import produtos
pagamento = 0 # conta a pagar no final 



def hamburguers():
    global pagamento
    #for produto in lista_produtos():
    #        print(f"[{produto.id}] {produto.nome} - R${produto.valor}")
    #return pagamento

def acompanhamentos():
    global pagamento
    return pagamento

def bebidas():
    global pagamento
    with open("cardapio_dados.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('bebida: '):
            hamburguers = line.strip('\n').split(': ')[1]
            print(hamburguers)    
    pass

def sobremesas():
    global pagamento
    with open("cardapio_dados.txt","r") as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('sobremesa: '):
            hamburguers = line.strip('\n').split('sobremesa: ')[1]
            print(hamburguers)    
    pass

def combos():
    pass
