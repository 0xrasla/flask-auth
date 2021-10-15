from flask_login import UserMixin
from . import db, bcrypt

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(200))
    
    def __init__(self, email, password, username) -> None:
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("UTF-8")
        
    @classmethod
    def authenticate(cls, email, password):
        found_user = cls.query.filter_by(email=email).first()
        if found_user:
            authenticate_user = bcrypt.check_password_hash(found_user.password, password)
            if authenticate_user:
                return found_user
        return False
    
    @classmethod
    def userexists(cls, email):
        return True if cls.query.filter_by(email=email).first() else False