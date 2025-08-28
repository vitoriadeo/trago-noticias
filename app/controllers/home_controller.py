from flask import Blueprint, render_template, request
import requests

from flask import current_app

bp = Blueprint("home", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/cadastrar", methods=["POST"])
def cadastrar():
    try:
        recaptcha_token = request.form.get("recaptcha-response")

        secret_key = current_app.config["RECAPTCHA_SECRET_KEY"]
        verification_url = "https://www.google.com/recaptcha/api/siteverify"
        payload = {"secret": secret_key, "response": recaptcha_token}

        response = requests.post(verification_url, data=payload)
        result = response.json()

        name = request.form["name"]
        termo = request.form["termo"]
        email = request.form["email"]
        frequencia = request.form["frequencia"]

        # coisas do db e outros babados vão aqui.

        if result["success"] and result["score"] >= 0.5:
            # logica do db aqui
            mensagem_sucesso = f"Alerta para '{termo}' criado com sucesso!"
            return render_template(
                "index.html", status="sucesso", mensagem=mensagem_sucesso
            )
        else:
            mensagem_falha = (
                "Falha na verificação reCAPTCHA. Tente novamente."
            )
        return render_template("index.html", status="falha", mensagem=mensagem_falha)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        mensagem_falha = "Vish! Ocorreu um erro interno."
        return render_template("index.html", status="falha", mensagem=mensagem_falha)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/privacy")
def privacy():
    return render_template("privacy.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")
