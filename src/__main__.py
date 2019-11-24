import argparse

from flask import Flask, jsonify
from flask_restplus import Api, Resource

if __name__ == "__main__":
    api = Api()
    app = Flask(__name__)
    api.init_app(app)

    parser = argparse.ArgumentParser(description='Basic Flask App')
    parser.add_argument('--port', type=int, default=5000,
                        help='Set server port.')
    parser.add_argument('--debug', action='store_true',
                        help='Debug mode.')
    args = parser.parse_args()

    ns = api.namespace('intro', description='Introduction')

    @ns.route('/')
    class HelloWorld(Resource):
        def get(self):
            return jsonify({'message': 'hello world'})

        def post(self):
            return jsonify({'success': True})

    todos_ns = api.namespace('todos', description='Todos')

    @todos_ns.route('/')
    class Todo(Resource):
        def get(self):
            return {"todos": [{"id": 1, "title": 'hello'}]}

    app.run(port=args.port, debug=args.debug)
