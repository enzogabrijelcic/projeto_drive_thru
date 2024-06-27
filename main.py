import time,os
import random, time, os
from cardapio import *
from formatação import *
from forma_pagamento import *
from usuario import Usuario
import login

#cadastro1 = Cadastro('marcio', '658989', '1234')
#cadastro2 = Cadastro('ze', '989', 'abc')
#list_cadastro = [dados_castro]


def ler_dados():
    lista_usuarios = []
    with open("projeto_drive_thru\dados_cadastro.txt",'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Usuario '):
            atributos = line.strip().split('Usuario: ')[1]
            nome = atributos.split(':')[1].split(',')[0]
            cpf = atributos.split(':')[2].split(',')[0]
            senha = atributos.split(':')[3]
            usuario1 = Usuario(nome,cpf, senha)
            lista_usuarios.append(usuario1)
    return lista_usuarios

    
  
def salvar_dados(nome, cpf, senha):
    with open('projeto_drive_thru\dados_cadastro.txt', 'a') as file:
        
        for nome1 in nome:
            file.write(f'nome: {nome1}\n')
        for cpf1 in cpf:
            file.write(f'cpf: {cpf1}\n')
        for senha1 in senha:
            file.write(f'senha: {senha1}\n')
       

def adicionar_usuario(usuarios):
    nome = input("Nome de usuário: ")
    cpf = input('digite o cpf: ')
    senha = input("Senha: ")
    usuarios.append(Usuario(nome, cpf, senha))

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
                pedido()
        print("[1] Adicionar mais um item"),zzz()
        print("[2] Verificar carrinho"),zzz()
        print("[3] Finalizar pedido.")
        x = input()
        zzz()
        clear_console()
        match x:
            case "1":
                pass
            case "2":
                verificar_carrinho()
            case "3":
                forma_pagamento()
                n_pedido = random.randrange(0,1000)
                forma_pagamento(n_pedido)
                exit()
            case _:
                typing("Invalido, reiniciando"),zzz()

def main():
    lista = ler_dados()
    
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
            escolha = input('Voce possui Cadastro? [1] Sim [2] Não \n')

            match escolha:
                case '1':
                    print('Voce selecionou efetuar Login')
                    nome = input('digite o nome:\n')
                    cpf = input('digite o cpf:\n')
                    senha = input('digite a senha:\n')
                    login.login_lista_cadastro(lista, nome , cpf, senha)

                case '2':
                    adicionar_usuario(lista)
                    salvar_dados(nome, cpf,senha)
                    print('Voce selecionou efetuar Cadastro')    


        elif opcao == '3':
            typing("Tenha um bom dia"),time.sleep(1)
            exit()
        
main()