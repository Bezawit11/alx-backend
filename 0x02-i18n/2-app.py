#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, request
from flask_babel import Babel


class Config:
    """"the flask app's configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])
