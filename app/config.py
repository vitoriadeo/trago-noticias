import os

class Config:
    SECRET_KEY = "minhachave"

class ProdConfig(Config):
    RECAPTCHA_SITE_KEY = os.environ.get('RECAPTCHA_SITE_KEY')
    RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')