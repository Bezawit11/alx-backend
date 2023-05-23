#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    a = request.query_string.decode('utf-8').split('&')
    j = {}
    for i in a:
        p = i.split('=')
        j[p[0]] = p[1]
    if 'locale' in j:
        if j['locale'] in app.config['LANGUAGES']:
            return j['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('4-index.html')
