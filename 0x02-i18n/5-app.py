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
        return users.get(int(a))
    return None


@app.after_request 
def before_request() -> None:
    """executed before every request"""
    u = get_user()
    a.user = u

@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    a = request.args.get('locale')
    if a in app.config['LANGUAGES']:
        return a
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
