class Usuario:
    def __init__(self, login, senha,):
        self.login = login
        self.senha = senha
        
        

dados = [
    Usuario("aluno", "123", ),
   

]


def buscar_usuario_por_login(login):
    for dado in dados:
        if dado.login == login:
            return dado

    return None


def criar(usuario):
    dados.append(usuario)
