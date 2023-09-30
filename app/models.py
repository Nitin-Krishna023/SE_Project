from flask_login import UserMixin
from datetime import datetime
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(20), unique=False, nullable=True)
    last_name = db.Column(db.String(20), unique=False, nullable=True)
    phone = db.Column(db.String(20), unique=False, default="")
    bio = db.Column(db.Text, nullable=True, default="")
    email = db.Column(db.String(100), nullable=True, default="")
    profile_picture = db.Column(db.String(256), nullable=False, default="")
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    stripe_customer_id = db.Column(db.Text, nullable=False, default="")

    events = db.relationship('Event', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.date_registered}')"

    def get_id(self):
        return str(self.id)
    
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=True, nullable=False)
    cinema = db.Column(db.Integer())
    location = db.Column(db.Integer())
    stripe_transaction_id = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __repr__(self):
        return f"Event('{self.name}', '{self.transaction_id}')"

    def get_id(self):
        return str(self.id)