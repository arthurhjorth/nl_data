from sqlalchemy.types import JSON, Date
from nl_data import db



class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    open_until = db.Column(Date)
    data_points = db.relationship('DataPoint', 'activity_data_points')

class ActivityDataPoints(db.Model):
    __tablename__ = 'activity_data_points'
    activity_id = db.Column(db.Integer(), db.ForeignKey('activity.id', ondelete='CASCADE'))
    datapoint_id = db.Column(db.Integer(), db.ForeignKey('data_point.id', ondelete='CASCADE'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    roles = db.relationship('Role', secondary='user_roles')
    # data_points  = AH: create a table for this?


    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY']
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.relationship('Activity', 'activity_data_points')