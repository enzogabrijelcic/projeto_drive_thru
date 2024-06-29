from usuario import Usuario

class GerenciadorUsuarios:
    arquivo_usuarios = 'usuario.txt'

    def __init__(self):
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        usuarios = {}
        try:
            with open(self.arquivo_usuarios, 'r') as f:
                for line in f:
                    usuario = Usuario.from_string(line)
                    usuarios[usuario.cpf] = usuario
        except FileNotFoundError:
            pass
        return usuarios

    def salvar_usuarios(self):
        with open(self.arquivo_usuarios, 'w') as f:
            for usuario in self.usuarios.values():
                f.write(usuario.to_string() + '\n')

    def cadastrar_usuario(self, nome, cpf, senha):
        if cpf in self.usuarios:
            return "Usuário já cadastrado com este CPF."
        self.usuarios[cpf] = Usuario(nome, cpf, senha)
        self.salvar_usuarios()
        return "Usuário cadastrado com sucesso!"

    def login(self, cpf, senha):
        if cpf in self.usuarios and self.usuarios[cpf].senha == senha:
            return f"Login bem-sucedido! Bem-vindo, {self.usuarios[cpf].nome}!"
        return "CPF ou senha incorretos."




    