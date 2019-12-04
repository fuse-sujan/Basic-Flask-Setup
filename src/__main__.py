import argparse

from flask import Flask, jsonify
from werkzeug.contrib.fixers import ProxyFix

from src.resources import api


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    api.init_app(app)

    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Basic Flask App')
    parser.add_argument('--port', type=int, default=5000,
                        help='Set server port.')
    parser.add_argument('--debug', action='store_true',
                        help='Debug mode.')
    args = parser.parse_args()

    app = create_app()
    app.run(port=args.port, debug=args.debug)
