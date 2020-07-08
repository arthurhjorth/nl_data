from sqlalchemy.types import JSON, Date
from nl_data import db



class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    open_until = db.Column(Date)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    organizations = db.relationship('Organization', secondary='user_orgs')
    admin = db.Column(db.Boolean, default=False)
    roles = db.relationship('Role', secondary='user_roles')
    data_points 


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)