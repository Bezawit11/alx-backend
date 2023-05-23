#!/usr/bin/env python3
"""Flask app"""


from flash import Flask
from flask_babel import Babel


app = Flask(__name__)
class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
babel = Babel(app)
app.config.from_object(Config)
