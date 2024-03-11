from flask_sqlalchemy import SQLAlchemy
from config.config import db
from datetime import datetime

class Client(db.Model):
    __tablename__ = "clients_table"
    client_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(12), nullable=True)
    cellphone = db.Column(db.String(50), nullable = True)
    registration_date = db.Column(db.Date)
    packages = db.relationship("Package", backref="client", lazy="dynamic")

    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.registration_date = datetime.now().date()

    def __repr__(self):
        return f"Cliente {self.name}, email {self.email}"
    
    def to_json(self):
        return {
        "client_id": self.client_id,
        "name": self.name, 
        "email": self.email,
        "cpf": self.cpf if self.cpf is not None else None,
        "registration_date": self.registration_date.strftime("%d/%m/%Y") if self.registration_date is not None else None, 
        "cellphone": self.cellphone if self.cellphone is not None else None } 
        
        
    def from_json(self, data_json):
        name = data_json.get('name')
        email = data_json.get('email')
        cpf = data_json.get('cpf') if data_json.get('cpf') is not None else None,
        registration_date = data_json('registration_date') if data_json('registration_date') is not None else None
        if registration_date:
            registration_date = datetime.strptime(registration_date, "%d/%m/%Y").date()

        #cellphone
        data_from_json = Client(name=name, email=email,
                               registration_date= registration_date)
        return data_from_json


