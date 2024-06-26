import time,os
from cardapio import *
from formatação import *

def pedido():
    while True:
        typing("Selecione o que gostaria de comprar")
        print("\n[1] Hamburguer."),zzz()
        print("[2] Acompanhamento."),zzz()
        print("[3] Bebidas."),zzz()
        print("[4] Sobremesas.")
        x = input("\n")
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
            case _:
                print("Invalido"),time.sleep(2)
        print("[1] Adicionar mais um item"),zzz()
        print("[2] Finalizar pedido.")
        x = input()
        match x:
            case "1":
                pass
            case "2":
                exit()
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
            pass
        elif opcao == '3':
            typing("Tenha um bom dia"),time.sleep(2)
            exit()
        else:
            print("Opção inválida.")
            clear_console()
main()