from flask import Blueprint, render_template

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/privacy')
def privacy():
    return render_template('privacy.html')