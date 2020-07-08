import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_data_point_doesnt_exist(data_point_id):
    if data_point_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(data_point_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# Todo
#   show a single todo item and lets you delete them
class DataPoint(Resource):
    def get(self, data_point_id):
        abort_if_data_point_doesnt_exist(data_point_id)
        return TODOS[data_point_id]
        return DataPoint.query.get(data_point_id) # TODO: implement data point db model

    def delete(self, data_point_id):
        abort_if_data_point_doesnt_exist(data_point_id)
        del TODOS[data_point_id]
        return '', 204

    def put(self, data_point_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[data_point_id] = task
        return task, 201


# Todo
#   show a single todo item and lets you delete them
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        data_point_id = 'data_point%d' % (len(TODOS) + 1)
        TODOS[data_point_id] = {'task': args['task']}
        return TODOS[data_point_id], 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
