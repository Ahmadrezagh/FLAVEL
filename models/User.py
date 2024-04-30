from database import db

class User(db.Model):
    __tablename__ = 'Users'
    # Define your model fields here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    

