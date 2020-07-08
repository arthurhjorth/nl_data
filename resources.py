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
