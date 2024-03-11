from flask_sqlalchemy import SQLAlchemy
from config.config import db
from flask_bcrypt import Bcrypt

class User(db.Model):
    __tablename__ = "users_table"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(250))
    email = db.Column(db.String(100))
    cellphone = db.Column(db.String(50))

    def __init__(self, name, password, email, cellphone):
        self.name = name
        self.password = self.encript_password(password)
        self.email = email 
        self.cellphone = cellphone

    def encript_password(self, non_encripted_password):
        bcrypt = Bcrypt()
        encripted_password = bcrypt.generate_password_hash(non_encripted_password)
        return encripted_password    

    def __repr__(self):
        return f"Usuário {self.name}, email {self.email}"
    
    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name, 
            "password": self.password,
            "email": self.email,
            "cellphone": self.cellphone            
        }

