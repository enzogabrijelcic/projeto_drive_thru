from cadastro import Cadastro 

def novo_cadastro():
    x = input("Nome: ")
    y = input("CPF: ")
    z = input("Senha: ")
    novo = Cadastro(x,y,z)
    with open('dados_cadastro.txt', 'a') as file:
        file.write(f'Nome: {novo.nome}, CPF: {novo.cpf}, Senha: {novo.senha}\n')