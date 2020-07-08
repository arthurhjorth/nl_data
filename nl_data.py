import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_restful import reqparse, abort, Api, Resource
import resources


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

##
## Actually setup the Api resource routing here
##
api.add_resource(resources.TodoList, '/todos')
api.add_resource(resources.Todo, '/todos/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
