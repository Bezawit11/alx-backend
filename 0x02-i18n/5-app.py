#!/usr/bin/env python3
"""Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """custom config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """gets user based on id"""
    a = request.args.get('login_as')
    if a:
        return users[int(a)]
    return None

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
    return render_template('5-index.html')
