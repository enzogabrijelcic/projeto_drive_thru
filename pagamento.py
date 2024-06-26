#formas de pagamento: cartão, pix, dinheiro
import random

def forma_pagamento(n_pedido):
    forma_pag = input('Qual a forma de pagamento?\n1. Cartão \n2. Dinheiro \n3. pix\n4. Cancelar pedido\n opção:')
    if forma_pag == '1':
        print(" cartão. pagamento Confirmado")
        print('seu pedido é nº: ', n_pedido)
    elif forma_pag == '2':
        print("Dinheiro. Pague no local.")
        print('Número do pedido será gerado após o pagamento')
    elif forma_pag == '3':
        print('Pix. chave pix:2a1sd6a51sd6a1sd6a51s6da1s\n processando...\n Pagamento confirmado')
        print('seu pedido é nº:', n_pedido)
    elif forma_pag == '4':
        print("Cancelar pedido.")
    else:
        print("Opção inválida.")
#pagamento finalizado, gera um numero de pedido, COMO gerar esse número??
n_pedido = random.randrange(0,1000)