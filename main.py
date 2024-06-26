import random
import time,os
from cardapio import *
from formatação import *
from pagamento import *
from pagamento import forma_pagamento
from cadastro import Cadastro
import login
import novo_cadastro
#cadastro1 = Cadastro('marcio', '658989', '1234')
#cadastro2 = Cadastro('ze', '989', 'abc')
list_cadastro = [novo_cadastro]



def pedido():
    while True:
        typing("Selecione o que gostaria de comprar")
        print("\n[1] Hamburguer."),zzz()
        print("[2] Acompanhamento."),zzz()
        print("[3] Bebidas."),zzz()
        print("[4] Sobremesas."),zzz()
        print("[5] Combos")
        x = input("")
        zzz()
        clear_console()
        match x:
            case "1":
                hamburguers()
            case "2":
                acompanhamentos()
            case "3":
                bebidas()
            case "4":
                sobremesas()
            case "5":
                combos()
            case _:
                print("Invalido"),time.sleep(2)
        print("[1] Adicionar mais um item"),zzz()
        print("[2] Verificar carrinho"),zzz()
        print("[3] Finalizar pedido.")
        x = input(),zzz()
        clear_console()
        match x:
            case "1":
                pass
            case "2":
                verificar_carrinho()
            case "3":
                n_pedido = random.randrange(0,1000)
                forma_pagamento(n_pedido)
            case _:
                typing("Invalido, reiniciando"),zzz()

def main():
    
    #if not login(usuarios):
    #    print("Usuário ou senha incorretos.")
    #    main()
    
    typing("Login realizado com sucesso!"),time.sleep(1)
    typing("Carregando..."),time.sleep(2)
    clear_console()
    while True:
        typing("Bem vindo ao aplicativo de fast food delivery.")
        zzz()
        print("[1] Fazer Pedido."),zzz()
        print("[2] Checar Cadastro."),zzz()
        print("[3] Sair")

        opcao = input("\n")
        zzz()
        clear_console()
        if opcao == '1':
            pedido()
        elif opcao == '2':
            escolha = input('Voce possui Cadastro? [1] Sim [2] Não \n')

            match escolha:
                case '1':
                    print('Voce selecionou efetuar Login')
                    cpf = input('digite o cpf:\n')
                    senha = input('digite a senha:\n')
                    login.login_lista_cadastro(list_cadastro, cpf, senha)

                case '2':
                    print('Voce selecionou efetuar Cadastro')    
                    

        elif opcao == '3':
            typing("Tenha um bom dia"),time.sleep(1)
            exit()

        

        
main()