from flask import Blueprint, render_template, request, flash
from app.form import Form
from ..services import alert_service
import bleach

import requests

from flask import current_app

bp_about = Blueprint("about", __name__)
bp = Blueprint("home", __name__)


# ROTAS/PÁGINAS
@bp.route("/", methods=["GET", "POST"])
def index():
    form = Form()

    if form.validate_on_submit():
        try:
            # WTFORMS
            name = bleach.clean(form.name.data, tags=[], strip=True)
            email = bleach.clean(form.email.data, tags=[], strip=True)
            word = bleach.clean(form.word.data, tags=[], strip=True)
            frequency = bleach.clean(form.frequency.data, tags=[], strip=True)

            # GOOGLE RECAPTCHA V3
            recaptcha_token = request.form.get("g-recaptcha-response")

            secret_key = current_app.config["RECAPTCHA_SECRET_KEY"]
            verification_url = "https://www.google.com/recaptcha/api/siteverify"
            payload = {"secret": secret_key, "response": recaptcha_token}

            response = requests.post(verification_url, data=payload)
            result = response.json()

            print("Resposta do Google reCAPTCHA:", response, result)

            if result["success"]:
                alert_service.handle_alert_submission(name, email, word, frequency)

                flash(f"Alerta para '{word}' criado com sucesso! Você receberá as novidades por e-mail.", 'confirmation')
                return render_template(
                    "index.html", form=form, status="sucesso")
            else:
                flash("Falha na verificação reCAPTCHA. Tente novamente.", 'error')
                return render_template(
                    "index.html", form=form, status="falha")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

            flash("Vish! Ocorreu um erro interno.", 'error')
            return render_template(
                "index.html", form=form, status="falha")

    return render_template("index.html", form=form)


@bp.route("/about")
def about():
    return render_template("about.html")

@bp_about.route("/about/guide")
def guide():
    return render_template("guide.html")

@bp.route("/privacy")
def privacy():
    return render_template("privacy.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")
