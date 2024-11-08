#!/usr/bin/env python3
"""A Basic Flask application"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """Set configuration variables for the Flask-Babel extension."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """Renders the index template."""
    render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
