import time,os
import random, time, os
from cardapio import *
from formatação import *
from forma_pagamento import *
from usuario import Usuario
import login
from login import GerenciadorUsuarios
valor = 0
def ler_dados():
    lista_usuarios = []
    with open("usuario.txt",'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.startswith('Usuario: '):
            atributos = line.strip().split('Usuario: ')[1]
            nome = atributos.split(':')[1].split(',')[0]
            cpf = atributos.split(':')[2].split(',')[0]
            senha = atributos.split(':')[3]
            usuario1 = Usuario(nome,cpf, senha)
            lista_usuarios.append(usuario1)
    return lista_usuarios

    
  
def salvar_dados(nome, cpf, senha):
    with open('usuario.txt', 'a') as file:
        
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
    global valor
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
                valor = hamburguers()
            case "2":
                valor = acompanhamentos()
            case "3":
                valor = bebidas()
            case "4":
                valor = sobremesas()
            case "5":
                valor = combos()
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
                forma_pagamento(valor)
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
            
            gerenciador = GerenciadorUsuarios()
    
            while True:
                print("\nMenu:")
                print("1. Cadastrar usuário")
                print("2. Login")
                print("3. Sair")
                
                escolha = input("Escolha uma opção: ")
                
                if escolha == "1":
                    nome = input("Digite seu nome: ")
                    cpf = input("Digite seu CPF: ")
                    senha = input("Digite a senha desejada: ")
                    mensagem = gerenciador.cadastrar_usuario(nome, cpf, senha)
                    print(mensagem)
                elif escolha == "2":
                    cpf = input("Digite seu CPF: ")
                    senha = input("Digite sua senha: ")
                    mensagem = gerenciador.login(cpf, senha)
                    print(mensagem)
                elif escolha == "3":
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

    
               

        elif opcao == '3':
            typing("Tenha um bom dia"),time.sleep(1)
            exit()
        
main()