from usuario import Usuario


def login_obj (cadastro:Usuario, nome,cpf, senha):
   
    if nome == cadastro.nome and cpf == cadastro.cpf and senha == cadastro.senha:
        return True
    else:
        return False
def login_lista_cadastro(list:list[Usuario], nome,cpf, senha):
    #varrer a lista de cadastro
    passou = False
    for cadastro in list:
        if login_obj (cadastro, nome,  cpf, senha):
            passou = True

    if passou == True:
        print("login com sucesso")
        return True
    else:
        print('Login incorreto')
        return False
        



    