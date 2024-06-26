from cadastro import Cadastro

def login_obj (cadastro:Cadastro):
    cpf = input('digite o cpf ')
    senha = input('digite a senha')
    if cpf == cadastro.nome and senha == cadastro.senha:
        return True
    else:
        return False
def login_lista_cadastro(list:list[Cadastro]):
    #varrer a lista de cadastro
    passou = False
    for cadastro in list:
        if login_obj (cadastro):
            passou = True

    if passou == True:
        print("login com sucesso")
        return True
    else:
        print('Login incorreto')
        return False
        



    