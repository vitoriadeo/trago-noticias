from flask import Blueprint, render_template, request
from app.form import Form

import requests

from flask import current_app

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    form = Form()

    if form.validate_on_submit():
        try:
            recaptcha_token = request.form.get("recaptcha-response")

            secret_key = current_app.config["RECAPTCHA_SECRET_KEY"]
            verification_url = "https://www.google.com/recaptcha/api/siteverify"
            payload = {"secret": secret_key, "response": recaptcha_token}

            response = requests.post(verification_url, data=payload)
            result = response.json()

            print("Resposta do Google reCAPTCHA:", response, result)

            name = form.name.data
            word = form.word.data
            email = form.email.data
            frequency = form.frequency.data

            # coisas do db e outros babados vão aqui.

            if result["success"] and result["score"] >= 0.5:
                # logica do db aqui
                mensagem_sucesso = f"Alerta para '{word}' criado com sucesso!"
                return render_template(
                    "index.html", form=form, status="sucesso", mensagem=mensagem_sucesso
                )
            else:
                mensagem_falha = "Falha na verificação reCAPTCHA. Tente novamente."
                return render_template(
                    "index.html", form=form, status="falha", mensagem=mensagem_falha
                )

        except Exception as erro:
            print(f"Ocorreu um erro: {erro}")

            mensagem_falha = "Vish! Ocorreu um erro interno."
            return render_template(
                "index.html", form=form, status="falha", mensagem=mensagem_falha
            )

    return render_template("index.html", form=form)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/privacy")
def privacy():
    return render_template("privacy.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")
