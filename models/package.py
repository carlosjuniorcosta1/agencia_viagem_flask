from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey
from datetime import datetime
from flask import jsonify

class Package(db.Model):
    __tablename__ = "packages_table"
    package_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    client_id = db.Column(db.Integer, ForeignKey('clients_table.client_id'), nullable=False)
    origin = db.Column(db.String(150), nullable=False)
    destination = db.Column(db.String(150), nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    registration_date = db.Column(db.Date)
    price = db.Column(db.Float, nullable=True)
    meals = db.Column(db.String(10), nullable= True)
    accommodation = db.Column(db.Boolean, nullable = True)
    travelers = db.Column(db.SmallInteger, default=1)
    clients = db.relationship("Client", backref="clients")

    def __init__(self, client_id, origin, destination, departure_date, 
                 return_date, price, meals, accomodation, travelers):
        self.client_id = client_id
        self.origin = origin
        self.destination = destination
        self.departure_date = datetime.strptime(departure_date, "%d/%m/%Y")
        self.return_date = datetime.strptime(return_date, "%d/%m/%Y") if return_date else None,
        self.registration_date = datetime.now().date()
        self.price = price
        self.meals = self.valid_meals(meals)
        self.accommodation = accomodation
        self.travelers = travelers  
    
    def valid_meals(self, meals):       
        if meals:
            valid_meals = {"C", "A", "J", "ALL"}
            meal_set = set(meals.split(','))
            if "ALL" in meal_set:
                return "ALL"
            else:
                meal_list = list(meal_set)
                meal_list.sort()
                if set(meal_list).issubset(valid_meals): 
                    return meal_list
                else:
                    raise ValueError("The options for meals are just: C (breakfast), A (lunch), J (dinner) or ALL (all inclusive)")
            
    def to_json(self):
        return {
            "package_id": self.package_id,
            "client_id": self.client_id,
            "destination": self.destination,
            "departure_date": self.departure_date.strftime("%d/%m/%Y") if self.departure_date is not None else None,
            "return_date": self.return_date.strftime("%d/%m/%Y") if self.return_date is not None else None, 
            "registration_date": self.registration_date.strftime("%d/%m/%Y") if self.registration_date is not None else None,
            "price": self.price,
            "meals": self.meals if self.meals is not None else None,
            "accomodation": self.accommodation if self.accommodation is not None else None,
            "origin": self.origin,
            "travelers": self.travelers 
        }

    def __repr__(self):
        return f"Pacote {self.package_id}, origem {self.origin}, destino {self.destination}, preço {self.price}"





