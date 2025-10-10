from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, AnyOf


class Form(FlaskForm):

    name = StringField(
        "Seu nome",
        validators=[
            DataRequired(message="Por favor, insira seu nome."),
            Length(min=2, max=100),
        ],
    )
    word = StringField(
        "Termo para monitorar",
        validators=[
            DataRequired(message="Você precisa nos dizer o que monitorar!"),
            Length(min=3, max=255, message="O termo deve ter pelo menos 3 caracteres."),
        ],
    )
    email = EmailField(
        "Endereço de e-mail",
        validators=[
            DataRequired(message="O campo de e-mail é obrigatório."),
            Email(message="Por favor, insira um e-mail válido."),
        ],
    )
    frequency = SelectField(
        "Frequência dos alertas",
        choices=[
            ("", "Selecione a frequência"),
            ("once", "Somente uma vez, quando uma novidade aparecer"),
            ("realtime", "Sempre que uma novidade aparecer"),
        ],
        validators=[
            DataRequired(message="Por favor, selecione uma frequência para o alerta."),
            AnyOf(
                values=[
                    ("once"),
                    ("realtime"),
                ],
                message="Por favor, escolha uma opção válida.",
            ),
        ],
    )
    submit_button = SubmitField("Criar alerta", render_kw={"class": "button"})
