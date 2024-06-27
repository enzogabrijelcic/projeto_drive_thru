from cardapio import pagamento
from numero_pedido_sequencial import *
import time
from formatação import *
pagamento = 0
n_pedido = gerar_numero_pedido()

def forma_pagamento():
    while True:
        forma_pag = typing('Qual a forma de pagamento?')
        print('1. Cartão \n2. Dinheiro \n3. pix\n4. Cancelar pedido')
        forma_pag = input()
        if forma_pag == '1':
            print("Pagamento confirmado com cartão.")
            time.sleep(1)
            print('Seu pedido é nº:', n_pedido)
            break

        elif forma_pag == '2':
            dinheiro = float(input("Informe a quantia em dinheiro: R$ "))
            if dinheiro >= pagamento:
                troco = dinheiro - pagamento
                print(f"Troco: R$ {troco:.2f}")
                print('Seu pedido é nº:', n_pedido)
                break
            else:
                print("Dinheiro insuficiente. Por favor, informe uma quantia suficiente.")

        elif forma_pag == '3':
            print('Pix Selecionado.')
            time.sleep(1)
            print('chave Pix:2a1sd6a51sd6a1sd6a51s6da1s')
            time.sleep(3)
            print("Processando pagamento",end = ""),slow_typing("...")
            print('seu pedido é nº:', n_pedido)
            break

        elif forma_pag == '4':
            print("Pedido cancelado.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            forma_pagamento()
