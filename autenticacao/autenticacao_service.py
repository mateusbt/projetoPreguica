from autenticacao.autenticacao_dao import buscar_usuario_por_login, criar


def autenticar(login, senha):
    usuario = buscar_usuario_por_login(login)

    if usuario == None:
        raise Exception("Usuário não cadastrado")

    return usuario.senha == senha


def salvar_usuario(usuario):
    dado = buscar_usuario_por_login(usuario.login)

    if dado != None:
        raise Exception("Usuário já cadastrado")

    criar(usuario)
