from flask_1 import db,login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model, UserMixin):
    id= db.Column(db.Integer,primary_key= True)
    username =db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    data_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    
    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.image_file}')"

class person(db.Model):
    id=db.Column(db.Integer,primary_key= True)
    name=db.Column(db.String(20),unique=True,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    lab_name=db.Column(db.String(20),nullable=False)