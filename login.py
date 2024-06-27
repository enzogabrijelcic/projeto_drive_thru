from cadastro import Cadastro

def login_obj (cadastro:Cadastro,cpf, senha):
   
    if cpf == cadastro.cpf and senha == cadastro.senha:
        return True
    else:
        return False
def login_lista_cadastro(list:list[Cadastro],cpf, senha):
    #varrer a lista de cadastro
    passou = False
    for cadastro in list:
        if login_obj (cadastro, cpf, senha):
            passou = True

    if passou == True:
        print("login com sucesso")
        return True
    else:
        print('Login incorreto')
        return False
        



    