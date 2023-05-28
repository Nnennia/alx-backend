#!/usr/bin/env python3
""""Function with the babel.localselector"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)


def get_locale():
    """"Get locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def index():
    """render index.html"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
