from flask_restplus import Resource, fields

from src.resources import api
from src.models import todo, TodoDAO

todo_ns = api.namespace('todos', description='Todos')


DAO = TodoDAO()
DAO.create({'task': 'Build an API'})
DAO.create({'task': 'Copy code from Flask RestPlus doc :P'})
DAO.create({'task': 'Give presentation'})


@todo_ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @todo_ns.doc('list_todos')
    @todo_ns.marshal_with(todo, as_list=True)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @todo_ns.doc('create_todo')
    @todo_ns.expect(todo, validate=True)
    @todo_ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@todo_ns.route('/<int:id>')
@todo_ns.response(404, 'Todo not found')
@todo_ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @todo_ns.doc('get_todo')
    @todo_ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @todo_ns.doc('delete_todo')
    @todo_ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @todo_ns.expect(todo)
    @todo_ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)
