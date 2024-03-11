from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey
from datetime import datetime

class Package(db.Model):
    __tablename__ = "packages_table"
    package_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    client_id = db.Column(db.Integer, ForeignKey('clients_table.client_id'))
    origin = db.Column(db.String(150))
    destination = db.Column(db.String(150))
    departure_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    registration_date = db.Column(db.Date)
    price = db.Column(db.Float)

    def __init__(self, client_id, origin, destination, departure_date, 
                 return_date, price):
        self.client_id = client_id
        self.origin = origin
        self.destination = destination
        self.departure_date = self.fill_dates(departure_date)
        self.return_date = self.fill_dates(return_date)
        self.registration_date = datetime.now().date()
        self.price = price 
    
    def fill_dates(self, date_dd_mm_yyyy):
        day, month, year = map(int, date_dd_mm_yyyy.split('/'))
        form_date = datetime(year, month, day)
        return form_date
    def to_json(self):
        return {
            "package_id": self.package_id,
            "client_id": self.client_id,
            "destination": self.destination,
            "departure_date": self.departure_date,
            "return_date": self.return_date, 
            "registration_date": self.registration_date,
            "price": self.price
        }

    def __repr__(self):
        return f"Pacote {self.package_id}, origem {self.origin}, destino {self.destin}, preço {self.price}"





