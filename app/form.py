from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField
from wtforms.validators import DataRequired, Email, Length, AnyOf


class Form(FlaskForm):
    name = StringField("Seu nome", validators=[DataRequired(), Length(min=2, max=100)])
    word = StringField(
        "Termo para monitorar",
        validators=[DataRequired(), Length(min=2, max=100)],
    )
    email = EmailField("Endereço de e-mail", validators=[DataRequired(), Email()])
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
                    ("diario"),
                    ("semanal"),
                    ("mensal"),
                    ("anual"),
                ],
                message="Por favor, escolha uma opção válida.",
            ),
        ],
    )
