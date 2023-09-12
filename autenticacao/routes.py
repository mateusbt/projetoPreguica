import flask as f
import autenticacao.autenticacao_service as auth_service
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from autenticacao.autenticacao_dao import Usuario

autenticacao_bp = f.Blueprint("autenticacao", __name__, url_prefix="/auth")


class LoginForm(FlaskForm):
    login = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=10)])


class RegistroForm(FlaskForm):
    login = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=10)])
    nome = StringField("Nome", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired(), Length(11)])


@autenticacao_bp.route("/registro", methods=["GET", "POST"])
def registro():
    registroForm = RegistroForm()

    if f.request.method == "GET":
        return f.render_template("registro.html", form=registroForm)

    if not registroForm.validate_on_submit():
        f.flash("Dados obrigatórios não preenchidos")
        return f.render_template("registro.html")

    usuario = Usuario(
        registroForm.login.data,
        registroForm.senha.data,
        registroForm.nome.data,
        "Aluno",
    )

    try:
        auth_service.salvar_usuario(usuario)
        f.flash("Usuário cadastrado com sucesso")
        return f.redirect(f.url_for("hello_world"))
    except:
        f.flash("Nome de usuário já cadastrado")
        return f.render_template("registro.html")


@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if f.request.method == "GET":
        return f.render_template("index.html", form=form)

    if not form.validate_on_submit():
        f.flash("Login ou senha não informada!")
        return f.redirect(f.url_for("hello_world"))

    try:
        if auth_service.autenticar(form.login.data, form.senha.data):
            f.session["usuario_logado"] = form.login.data
            return f.redirect(f.url_for("main"))
    except:
        f.flash("Usuário não cadastrado!")
        return f.redirect(f.url_for("hello_world"))

    f.flash("Login ou senha inválida!")
    return f.redirect(f.url_for("hello_world"))


@autenticacao_bp.route("/logout")
def logout():
    del f.session["usuario_logado"]
    return f.redirect(f.url_for("hello_world"))
