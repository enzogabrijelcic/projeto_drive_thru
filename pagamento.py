#formas de pagamento: cartão, pix, dinheiro
import time
from formatação import *
def forma_pagamento(n_pedido):
    forma_pag = typing('Qual a forma de pagamento?')
    print('1. Cartão \n2. Dinheiro \n3. pix\n4. Cancelar pedido')
    forma_pag = input()
    if forma_pag == '1':
        print("Cartão Selecionado.") 
        time.sleep(1)
        print("Processando pagamento",end = ""),slow_typing("...")
        print('nº do pedido: ', n_pedido)
    elif forma_pag == '2':
        print("Dinheiro Selecionado")
        time.sleep(1)
        print("Pague no local")
        print('Número do pedido será gerado após o pagamento')
    elif forma_pag == '3':
        print('Pix Selecionado.')
        time.sleep(1)
        print('chave Pix:2a1sd6a51sd6a1sd6a51s6da1s')
        time.sleep(3)
        print("Processando pagamento",end = ""),slow_typing("...")
        print('seu pedido é nº:', n_pedido)
    elif forma_pag == '4':
        print("Pedido cancelado.")
        exit()
    else:
        print("Opção inválida.")
        forma_pagamento()
#pagamento finalizado, gera um numero de pedido, COMO gerar esse número??

