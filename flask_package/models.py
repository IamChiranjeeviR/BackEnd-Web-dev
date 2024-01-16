from flask_package import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=True, nullable=False)
    EmailId = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f"user('{self.userName}','{self.EmailId}')"